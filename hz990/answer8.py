a = {'first':[2,1],'second':[2,3],'third':[3,4]}

# Swap the values of the 'first' and 'third' keys
cache = a['first']
a['first'] = a['third']
a['third'] = cache
print a

# Sort the elements of the list with key 'third'
a['third'].sort()
print a

# Add a new key 'fourth' with the value of the key 'second' 
a['fourth'] = a['second']
print a

# Delete the key/value pair 'second'
del a['second']
print a