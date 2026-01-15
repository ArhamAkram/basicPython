import heapq
import itertools
import threading
import time
from concurrent.futures import ThreadPoolExecutor


class Scheduler:
    def __init__(self, clock=None, worker=None):
        self._clock = clock or time.monotonic
        self._worker = worker or ThreadPoolExecutor(max_workers=4)
        self._owns_worker = worker is None
        self._lock = threading.Lock()
        self._cv = threading.Condition(self._lock)
        self._tasks = {}
        self._heap = []
        self._counter = itertools.count(1)
        self._stop = False
        self._thread = None

    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop = False
        self._thread = threading.Thread(target=self._run, name="scheduler", daemon=True)
        self._thread.start()

    def stop(self):
        with self._cv:
            self._stop = True
            self._cv.notify_all()
        if self._thread:
            self._thread.join(timeout=2)
        if self._owns_worker and hasattr(self._worker, "shutdown"):
            self._worker.shutdown(wait=True)

    def schedule(self, delay_seconds, fn):
        if delay_seconds < 0:
            raise ValueError("delay_seconds must be >= 0")
        run_at = self._clock() + delay_seconds
        task_id = next(self._counter)
        with self._cv:
            self._tasks[task_id] = (run_at, fn)
            heapq.heappush(self._heap, (run_at, task_id))
            self._cv.notify()
        return task_id

    def cancel(self, task_id):
        with self._cv:
            if task_id not in self._tasks:
                return False
            del self._tasks[task_id]
            self._cv.notify()
            return True

    def wake(self):
        with self._cv:
            self._cv.notify_all()

    def _pop_due(self, now):
        due = []
        while self._heap and self._heap[0][0] <= now:
            run_at, task_id = heapq.heappop(self._heap)
            task = self._tasks.pop(task_id, None)
            if task is None:
                continue
            _, fn = task
            due.append(fn)
        return due

    def _run(self):
        while True:
            with self._cv:
                if self._stop:
                    return
                now = self._clock()
                due = self._pop_due(now)
                if not due:
                    if not self._heap:
                        self._cv.wait()
                        continue
                    wait = self._heap[0][0] - now
                    if wait > 0:
                        self._cv.wait(timeout=wait)
                        continue
            for fn in due:
                self._worker.submit(fn)
