"""This is the answers for question 8"""


d={'first':[2,1],'second':[2,3],'third':[3,4]}

#part (a)
#assume that the dictionary is called 'd' in this example
d['first'],d['third']=d['third'],d['first']


#part (b)
d['third'].sort()

#part (c)
d['fourth']=d['second']

#part (d)
del  d['second']

print d

