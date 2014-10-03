###############################
#                             #
#       Answer 8              #
# by Maya Rotmensch (mer567)  #
#                             #
###############################


a = {'first': [2,1],'second':[2,3], 'third':[3,4]}

a['first'], a['third'] = a['third'],a['first'] #8.a


a['third'].sort() #8.b

a['fourth'] = a['second'] #8.c

a.pop('second') #8.d

print "final dictionary", a
