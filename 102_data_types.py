# strings

# these are a list of characters put together in a list
# defined by '' or ""

my_string = "amazing grilled fish"

print(my_string)
print(type(my_string))

# joining of 2 strings
# concatenation
first_name = 'Boris'
last_name = 'May'

print(first_name +  ' ' + last_name)
# you can just add them

full_name = first_name +  ' ' + last_name
print(full_name)

#interpolation
#inject a string into another string

name = 'Lana'
welcome_message = "welcome to the dangerzone!"

print(f"{name},welcome to the dangerzone!")
#place an f behind the string and use {} inside the string to interpolate the variables/python






