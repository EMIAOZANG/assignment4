d={'first':[2,1],'second':[2,3],'third':[3,4]}

d['first'],d['third']=d['third'],d['first']
#print('swap the values of the first and third keys')


d['third'].sort()
#print('sort the elements of the list with key third')

d['forth']=d['second']
#add a new key forth with the value of the key second')

del d['second']
#print('delete the key/value pair second')
print('the final dictionary')
print d



