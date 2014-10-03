d = {'first':[2,1], 'second':[2,3], 'third':[3,4]}
a = d['first']
d['first'] = d['third']
d['third'] = a
d['third'].sort()
d['fourth']=d['second']
del d['second']
print d 
