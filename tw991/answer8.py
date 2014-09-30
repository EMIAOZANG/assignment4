a={'first':[2,1],'second':[2,3],'third':[3,4]}
temp=a['third']
a['third']=a['first']
a['first']=temp
a['third'].sort()
a['fourth']=a['second']
del a['second']
print a
