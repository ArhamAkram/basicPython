import threading
import time
from unittest.mock import Mock

import pytest

from scheduler import Scheduler


class FakeClock:
    def __init__(self, start=0.0):
        self._now = start
        self._lock = threading.Lock()

    def now(self):
        with self._lock:
            return self._now

    def advance(self, seconds):
        with self._lock:
            self._now += seconds


def wait_until(predicate, timeout=1.0):
    end = time.monotonic() + timeout
    while time.monotonic() < end:
        if predicate():
            return True
        time.sleep(0.01)
    return False


def test_delayed_execution_not_before_due():
    clock = FakeClock(start=100.0)
    worker = Mock()
    scheduler = Scheduler(clock=clock.now, worker=worker)
    scheduler.start()
    try:
        scheduler.schedule(10, lambda: None)
        scheduler.wake()
        assert not wait_until(lambda: worker.submit.call_count > 0, timeout=0.1)

        clock.advance(9)
        scheduler.wake()
        assert not wait_until(lambda: worker.submit.call_count > 0, timeout=0.1)

        clock.advance(1)
        scheduler.wake()
        assert wait_until(lambda: worker.submit.call_count == 1)
    finally:
        scheduler.stop()


def test_invalid_scheduling_time_raises():
    scheduler = Scheduler(clock=time.monotonic, worker=Mock())
    with pytest.raises(ValueError):
        scheduler.schedule(-0.1, lambda: None)


def test_concurrent_task_dispatch():
    worker = Mock()
    scheduler = Scheduler(worker=worker)
    scheduler.start()
    total = 50
    threads = []
    barrier = threading.Barrier(5)

    def schedule_batch(count):
        barrier.wait()
        for _ in range(count):
            scheduler.schedule(0, lambda: None)

    try:
        for _ in range(5):
            t = threading.Thread(target=schedule_batch, args=(total // 5,))
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        scheduler.wake()
        assert wait_until(lambda: worker.submit.call_count == total)
    finally:
        scheduler.stop()


def test_cancellation_before_due_prevents_dispatch():
    clock = FakeClock(start=0.0)
    worker = Mock()
    scheduler = Scheduler(clock=clock.now, worker=worker)
    scheduler.start()
    try:
        task_id = scheduler.schedule(5, lambda: None)
        assert scheduler.cancel(task_id) is True
        clock.advance(10)
        scheduler.wake()
        assert not wait_until(lambda: worker.submit.call_count > 0, timeout=0.2)
        assert worker.submit.call_count == 0
    finally:
        scheduler.stop()


def test_cancel_after_dispatch_returns_false():
    worker = Mock()
    scheduler = Scheduler(worker=worker)
    scheduler.start()
    try:
        task_id = scheduler.schedule(0, lambda: None)
        scheduler.wake()
        assert wait_until(lambda: worker.submit.call_count == 1)
        assert scheduler.cancel(task_id) is False
    finally:
        scheduler.stop()


def test_concurrent_cancelation_boundary():
    clock = FakeClock(start=0.0)
    worker = Mock()
    scheduler = Scheduler(clock=clock.now, worker=worker)
    scheduler.start()
    try:
        task_ids = [scheduler.schedule(5, lambda: None) for _ in range(20)]
        to_cancel = set(task_ids[:10])

        def cancel_tasks():
            for task_id in to_cancel:
                scheduler.cancel(task_id)

        threads = [threading.Thread(target=cancel_tasks) for _ in range(3)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        clock.advance(5)
        scheduler.wake()
        assert wait_until(lambda: worker.submit.call_count == 10)
    finally:
        scheduler.stop()
