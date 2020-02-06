student1 = {
    'name':'Morty',
    'stream':'universal quest',
    'grade':12
}

student2 = {
    'name':'Summer',
    'stream':'Terrestial quest',
    'grade':20
}
#list of dicitionaries
students_list = [student1, student2]

#print(students_list[1])

#Dictionary of dictionaries
students_dictionary = {
    'student1': { 'name':'Morty', 'stream':'universal quest', 'grade':12 },
    'student2':student2
}

# use the list to print the individual student names
#use by index
ind_student1 = students_list[0]
print(ind_student1)
print(type(ind_student1))
print(ind_student1.keys())
print(ind_student1['name'])

ind_student2 = students_list[1]
print(ind_student2)
print(ind_student2['name'])


# --> morty
#--> summer
# use the dictionary to print the individual student names

print(students_dictionary.keys())
print(students_dictionary['student1'])
# student1_nesteddated =


nested_other_list = ['vales', 'losts of values']
nested_data = {'example': 'lots of data'}
# I have a dictionary with embeded data
# I want get the value of the first key and save it in a variabke
# print(nested_data.values())
# print(nested_other_list[1])
retrieved_data = nested_data['example']
#print(retrieved_data)
#print(nested_data['example'])
# Look into this value and extra more data

students_dictionary = {
    'student1': { 'name':'Morty', 'stream':'universal quest', 'grade':12 },
    'student2':student2
}


first_student_in_dic = students_dictionary['student1']
#print(first_student_in_dic)

individual_name = first_student_in_dic['name']
#print(individual_name)

second_student_in_dic = students_dictionary['student2']
#print(second_student_in_dic)

individual_name2 = second_student_in_dic['name']
#print(individual_name2)

# exercise
#define a dictionary with the following keys:
#beginning
#middle
#end
#heroine/hero
#populate the values of the keys, with a story broken into the start, middle, end.
#use your heroine as well
#print the story using by calling your dictionary keys individually
# interpolate!

story_dictionary = {
    'heroine':'laila',
    'beginning':'wanted really badly to go to the park',
    'middle':'But it became too late in the day to go',
    'end':' She decide to stay back home and watch netflix'
}
print(f"({story_dictionary['heroine']},{story_dictionary['beginning']},{story_dictionary['middle']},{story_dictionary['end']}")


the_beginning = story_dictionary
#print(the_beginning)
#print(the_beginning['beginning'])

the_middle = story_dictionary
#print(the_middle)
#print(the_middle['middle'])

the_end = story_dictionary
#print(the_end)
#print(the_end['end'])


#print()











