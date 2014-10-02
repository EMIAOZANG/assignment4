a = {'first':[2,1],'second':[2,3],'third':[3,4]}
#a. swap values of 'first' and 'third' keys
b = a['first']
a['first'] = a['third']
a['third'] = b
#b. sort the elements of the list with key third
a['third'].sort()
#c. Add a new key fourth with the value of the key second
a['fourth']=a['second']
#d. Delete the key/value pair second
del a['second']
print a