
my_age=24
my_name="Nuevo"
my_height = 1.8469E2
my_address = "419 Viger Est"
my_bool= True
my_imagination = 4 + 99j
my_binary= 0b1010
my_hex=0xF
test_int1 =0
test_int2 =0



print(type(my_bool))
print(my_imagination,my_imagination.real,my_imagination.imag,type(my_height))
print(my_age)
print(type(my_imagination))
print(my_imagination.__sizeof__())
print(bool(my_address))
height= int(input("Input height: "))
base =int(input("Input base: "))
base2 =int(input("Enter the smaller base: "))
Area = ((base2 + base)/2)*height
print("The area of the trapezium: ", Area)
