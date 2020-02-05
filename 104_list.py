# list
# defining a list
#syntax is [] for list
#Lists are organised using index which is shown below
# name_list = [   0    ,  1   ,      2   , 3  ]
#crazy_landlords = []
crazy_landlords = []
print(type(crazy_landlords))


# we can dynamically define a list or redefine it
crazy_landlords = ['Mr Richards', 'Raj', 'Mr Shirik', 'Zwen', 'Zemu']

# Access an object in a list
#Lists are organized using Index
# name_list = [   0    ,  1   ,      2   , 3  ]
# to access landlorj, we need the index number 1.
#crazy_landlords = ['Mr Richards', 'Raj', 'Mr Shirik', 'Zwen', 'Zemu']

print(crazy_landlords[1])
print(crazy_landlords[4])

# We can also refine at a specific index
# Change Zemu to Zumuna
print('changing index number 4 to zumuna')
crazy_landlords[4] = 'Zumuna'
print(crazy_landlords)


#print all of list
print(crazy_landlords)

#print the last one
print(crazy_landlords[-1])

#another way is to get the length and make into an index
length_list = len(crazy_landlords)
last_index = length_list - 1
print(crazy_landlords[last_index])


#adding a record to the list
#.append(object)
crazy_landlords.append('lana')
print(crazy_landlords)

#what if we need to add a record on a specific index
#we insert by
#.insert()
crazy_landlords.insert(2, 'Mr.Paiva')
print(crazy_landlords)

# remove item from list according to value
#.remove(arg) --> returns list without the value or arg
crazy_landlords.remove('Zwen')
print(crazy_landlords)

#remove using index - or last entry
#.pop()

crazy_landlords.pop() #removes last entry on last index
print(crazy_landlords)

#remove specific index
crazy_landlords.pop(1)  #removing raj from the list
print(crazy_landlords)

# we can have mixed data list
hybrid_list = ['JSON', 'Jason', 13, 53, [1, 2]]

print(hybrid_list)

#Tuples
#An immutable list
my_tuple = (2, 'hello', 22, 'more values')
print(my_tuple)
print(my_tuple[2])
#my_tuple[0] = 10 --> this breaks as we are trying to change the tuple

print(crazy_landlords)
#Range slicing
print(crazy_landlords[0:1]) # 0 to 1, not inclusive of 1
print(crazy_landlords[1:2]) # 1 to 2, not inclusive of 2


example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jumping/slicing
#syntax is [N:X:M]
#N is where it starts
#X is where it stops
#M is the length it jumps
print(example_list[0:5:3])

#we need more info in our landlords

crazy_landlords = ['Mr Richards', '0784124908', 'Raj', '0573928505', 'Mr Shirik', 'Zwen', 'Zemu']

#we need to add more data!

















