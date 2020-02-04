# Numerical date types
 #ints, long, float, complex
 # these are numerical types which can use numerical operators

 # complex and long we dont use as much
 # complex are built with imaginary numbers
  # an example would be if you need to track 2 seperate currencies in one variable

# long are just integers of unlimited size

#int and floats
#int stands for integers and are whole numbers
#floats are numbers with decimal places

#ints
my_int = 10
print(my_int)
print(type(my_int))

#float
my_float = 10.0
print(my_float)
print(type(my_float))


#operators - add subtract divide multiple and modulud

num1 = 12
num2 = 21
print(num2 + num1)
print(num2 - num1)
print(num2 * 2)

#modulus returns remainder
print(10%3)
print (22%3)
print(20%3)

print(20//3) # removes remainder

# comparison  operators --> boolean values
## ==  - equating things on both sides
## </> - bigger and smaller than
## <= - smallerthan or equals to
## =>  - greater than or equals to
## != - not equal to
## is - equates if some this is something
## is not - equates if something is not

my_variable = 10
my_variable2 = 13

print(my_variable == my_variable2)
print(my_variable == 10)
print(my_variable < my_variable2)
print(my_variable > my_variable2)
print(my_variable <= my_variable2)

print(my_variable is 10)
print(my_variable is not 13)

# Booleans
#True or false
#Binary true or false
print(type(True))
print(type(False))

# None
print(None)
print(type(None))

print(0 == None)

#Operators, Logical & and Logical or
a_var = True
b_var = False
#logical and & requires both sides to be true to result in true
#syntax- both sides need to be true
# (assertion_ a & assertion_b) --> boolean
print(a_var & True)
print(a_var & False)

#Logical or, only one side needs to be true to return true:
print('this will be true>>>')
print(True or False)

print()


