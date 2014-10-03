d={'first':[2,1], 'second':[2,3], 'third':[3,4]}

d['first'],d['third']=d['third'],d['first']
d['third'].sort()
d['fifth']=d['second']
del d['second']

print (d)