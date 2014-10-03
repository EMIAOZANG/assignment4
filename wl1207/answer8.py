dict={'first':[2,1],'second':[2,3],'third':[3,4]}
temp=dict['first']
dict['first']=dict['third']
dict['third']=temp
print dict

dict['third'].sort()
print dict

dict['fourth']=dict['second']
print dict

del dict['second']
print dict
