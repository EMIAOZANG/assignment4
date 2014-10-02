#answer8.py
#im965 program for assignment 04, question 08

#!/usr/bin/env python

#operate on a list to get the desired final list
d={'first':[1,2],'second':[2,3],'third':[3,4]}
print d

# a
temp=d['first']
d['first']=d['third']
d['third']=temp
print d

# b
d['third'].sort()
print d

#c
d['fourth']=d['second']
print d

# d
del d['second']
print d



