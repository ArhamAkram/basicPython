import math

print("What do you want to do")
print("0 - Km to Miles")
print("1 - Miles to Km")
print("2 - Find the area of a circle")
print("3 - Find the area of a cube")
print("4- Find the value of the root of a quadratic function")

user_input = input("Enter the corresponding number: ")



if user_input == "0" :
    user_km =  input("Enter the number of Km: ")
    print("value in miles is ", 0.621371*int(user_km))
elif user_input == "1":
    user_miles = input("Enter the number of Miles: ")
    print("value in km is ", (int(user_miles)/0.621371))
elif user_input == "2":
    user_radius = input("Enter the value of radius: ")
    print("The area of the circle is", math.pi*(int(user_radius)**2))
elif user_input == "3":
    user_cube_side = input("Enter the value of a side: ")
    print("The area of the cube is", 6*(int(user_cube_side)**2))
elif user_input == "4":
    print("the quadratic function is ax^2 + bx + c = 0")

    quadratic_a = input("Enter the value of a: ")
    quadratic_b = input("Enter the value of b: ")
    quadratic_c = input("Enter the value of c: ")


    delta = (int(quadratic_b)**2) - 4*(int(quadratic_a))*(int(quadratic_c))
    if delta < 0:
        print("roots are unavailable, delta negative")
        exit()

    root_1 = ((-int(quadratic_b)) + math.sqrt(delta))/(2*(int(quadratic_a)))
    root_2 = ((-int(quadratic_b)) - math.sqrt(delta)) / (2 * (int(quadratic_a)))
    print("root 1 of the polynomial is:", root_1)
    print("root 2 of the polynomial is:", root_2)

else:
    print("Wrong number was selected")
