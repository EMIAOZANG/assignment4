# Peter Li
# Homework 4, Question 8


# Set dict values

dict8 = {'first': [2,1], 'second': [2,3], 'third': [3,4]}

# swap values for first and third key

tmpList = dict8['first']
dict8['first'] = dict8['third']
dict8['third'] = tmpList

# sort the elements of the list with key third

dict8['third'].sort()

# add key 'fourth' with value of the key second

dict8['fourth'] = dict8['second']

# delete the key/value pair 'second'

del dict8['second']

print dict8