#conditional statements example

a=20
b=10
w = int(input("Enter a number: "))
if b>a:
    print("condition is true")

if w >= 0:
    print("Inputted number is positive")
else:
    print("Inputted is negative")

#Compound conditional statements (and, not, or)
# and: both conditions need to be true

input2 = int(input("Enter a number between 50 and 100: "))
if input2 >= 50 and input2 <= 100:
    print("Your input corresponds to the conditions")
else:
    print("You have inputted the wrong number")

# or: 1 condition needs to be true

# not: inverse the condition output, or condition.

# Check the difference between 2 numbers.

number1 = 100
number2 = 140

if number1 > number2:
    print(number1 - number2)
else:
    print(number2 - number1)

# Check if the number is odd or even.

number3 = 11
if number3 % 2 == 1:
    print("number is odd")
else:
    print("number is even")

# Check if the person is eligible ot vote

ageOfCitizen = 12

if ageOfCitizen >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Check the person's age is eligible to work or not.

if ageOfCitizen >= 18 and ageOfCitizen <= 60:
    print("Eligible to work")
else:
    print("Not eligible to work")

# discount challenge

clientPurchase = float(input("Enter the purchase price of the customer: "))

if clientPurchase <= 1000:
    print("The discounted price is ", clientPurchase*0.9)
elif clientPurchase > 1000 and clientPurchase <= 5000:
    print("The discounted price is ", clientPurchase * 0.8)
elif clientPurchase > 5000 and clientPurchase <= 10000:
    print("The discounted price is ", clientPurchase * 0.7)
elif clientPurchase > 10000:
    print("The discounted price is ", clientPurchase * 0.5)

