# Dictionaries
# we need to know where our crazy landlords live! we need more information
# introducing dictionaries
#Dictionaries are organized using key value pairs
#like a real dictionary
# if you want to look up the word 'omnipresent' you dont start ready the dictionary from 'A' all the way to 'o'

#syntax
#my_dictionary = {
#   'key': 'value'
#    'other_key: 'values'}

#define a simple dictionary
my_crazy_x_landlord = {
    'name': 'Laila',
    'phone' : '07510920591'
}

#Create one dictionary
my_crazy_x_landlord = {
    'name': 'Laila',
    'phone' : '07510920591'
}

#create a new key value pair
my_crazy_x_landlord['address'] = 'Fez, Morocco'
#Read all data of dictionary
print(my_crazy_x_landlord)
#read one entry in a dictionary (read the value of one key)
print(my_crazy_x_landlord['phone'])
#update the value in a key
my_crazy_x_landlord['phone'] = '+7510920591'
print(my_crazy_x_landlord['phone'])
# destroy one key value pair
my_crazy_x_landlord.pop('address')
print(my_crazy_x_landlord)

#getting all keys out
keys = my_crazy_x_landlord.keys()
print(keys)

values = my_crazy_x_landlord.values()
print(values)








