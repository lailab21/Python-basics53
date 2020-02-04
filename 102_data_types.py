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

#special methods for strings
my_string = "  hello this is an amazing string"

# .count
print(my_string.count('i'))

# .strip() removes traiiling white space
print(my_string)
print(my_string.strip())

# len() - function not a method
print(len(my_string))
print(len(my_string.strip()))

#.capitalize()
print(my_string.strip().capitalize())

# a method to make everything caps

# a method to make everything lower
# a method to separate the string into several strings.

print(my_string.upper())
print(my_string.lower())
print(my_string.split())















