#loops repeating statements
from math import factorial

#while loop
#print hello 10 times
count = 1
while count<11:
    print(count, "Hello")
    count+=1

#print the digits in reverse

reversed_number=123456
while reversed_number > 0:
   print(reversed_number % 10)
   reversed_number = reversed_number//10

#multiplication table

userNumber = int(input("Input a number to see it's multiplication table: "))
multiplierCount=1
while multiplierCount<11:
    print(userNumber, "X", multiplierCount," = ", userNumber*multiplierCount)
    multiplierCount+=1

# Count the number of a digit inside a number

digitCountedNumber = 1097846294
digitCount=0
while digitCountedNumber > 0:
   digitCountedNumber = digitCountedNumber // 10
   digitCount+=1
digitCountedNumber = 1097846294
print("The number of digits is ",digitCountedNumber, "is",digitCount)

# Sum the digit of a number

sumDigitNumber = 123
digitSum = 0

while sumDigitNumber > 0:
    digitSum += sumDigitNumber % 10
    sumDigitNumber = sumDigitNumber//10

sumDigitNumber = 123
print("The sum of digits of ",sumDigitNumber, "is",digitSum)


#Check if a number is a palindrome

numberPal1 = 1221
numberPal2 = 1981
checkPal = 0
while numberPal1 > 0:

    checkPaltemp = (numberPal1 % 10)
    numberPal1 = numberPal1 // 10
    checkPal = checkPal * 10+ checkPaltemp
numberPal1 = 1221
if checkPal == numberPal1:
    print(numberPal1, "is a palindrome")
else:
    print( print(numberPal1, "is not a palindrome"))

checkPal = 0
while numberPal2 > 0:

    checkPaltemp = (numberPal2 % 10)
    numberPal2 = numberPal2 // 10
    checkPal = checkPal * 10 + checkPaltemp

numberPal2 = 1981
if checkPal == numberPal2:
    print(numberPal2, "is a palindrome")
else:
    print( print(numberPal2, "is not a palindrome"))

#sum the number provided by user

numOfInputs = int(input("Enter the number of numbers of you want to sum: "))
q=0
sumInput = 0
while q<numOfInputs:

    sumInput += int(input("Enter a number: "))
    q +=1

print(sumInput)

#Find the maximum value within a list of number provided

numOfInputs2 = int(input("Enter the list of numbers of which you would like max: "))
q2=0
maxOfInputs = 0
while q2<numOfInputs2:

    userInput2 = int(input("Enter a number: "))
    if userInput2 > maxOfInputs:
        maxOfInputs = userInput2

    q2 += 1

print(maxOfInputs)

# continue statement statement restarts loop
# pass statement means do nothing

#for loops

msg= "hello"

for x in msg:
    print(x)

# multiplication table using for loop

forLoopMult = 5

for i in range (1,11):
    print(forLoopMult, "X", i,"=", forLoopMult*i )

#find the factorial of a number

factorialInput = int(input("Enter the number for which you want the factorial: "))
for i in range(factorialInput,2,-1):
    factorialInput = factorialInput*(i-1)

print(factorialInput)

# AP series

apSeriesCommonDiff = int(input("Enter the common difference between terms: "))
apSeriesStartingTerm =  int(input("Enter the starting term: "))
apSeriesNumberOfTerms =  int(input("Enter the number of terms: "))
currentTerm = apSeriesStartingTerm

for w in range(apSeriesNumberOfTerms):
    print(currentTerm)
    currentTerm += apSeriesCommonDiff

#fibonacci series

fibSeriesNumberOfTerms =  int(input("Enter the number of terms: "))
fibTerm1 = 0
fibTerm2 = 1
print(fibTerm1)
print(fibTerm2)
for q in range(fibSeriesNumberOfTerms-2):
    fibTerm3 = fibTerm1 + fibTerm2
    print(fibTerm3)
    fibTerm1=fibTerm2
    fibTerm2=fibTerm3

#find the factors of a number

factorsCheckInput = int(input("Enter a number to its factors: "))

for i in range(1, factorsCheckInput + 1):
    if factorsCheckInput % i == 0:
        print(i, "is a factor of", factorsCheckInput)
    else:
        pass

#check if number is prime

primeCheckInput = int(input("Enter a number to see if it is a prime number: "))
factorCount = 0
for i in range(1, primeCheckInput + 1):
    if primeCheckInput % i == 0:
        factorCount +=1
    else:
        pass

if factorCount == 2:
    print(primeCheckInput,"is a prime number")
else:
    print(primeCheckInput, "is not a prime number")

#pass and else statement

for i in range (0,10):
    pass
else:
    print("program completed")

#nested loop practice, print all the prime number from 1-100


for i in range (1,100):
    factorCount2=0
    for j in range(1,i+1):
        if i % j ==0:
            factorCount2+=1

    if factorCount2 == 2:
            print(i)