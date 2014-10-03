d={'first':[2,1], 'second':[2,3],'third':[3,4]}

#a
a={}
a['first']=d['third']
a['third']=d['first']
a['second']=d['second']

#b
a['third'].sort()

#c
a['fourth']=a['second']

#d
del a['second']

print a 



