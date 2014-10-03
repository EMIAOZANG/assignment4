d1 = {'first': [2,1], 'second': [2,3], 'third': [3,4]}
a = d1['first'] 
d1['first'] = d1['third']
d1['third'] = a

d1['third'].sort()

d1['fourth'] = d1['second']

del d1['second']

print d1
