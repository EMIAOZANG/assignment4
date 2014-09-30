# coding: utf-8
d={'first':[2,1],'second':[2,3],'third':[3,4]}
tmp = d['first']
d['first']=d['third']
d['first'] = d['third']
d['third'] = tmp
d['third'].sort()
d['fourth'] = d['second']
del d['second']
print 'The final dictionary: ', d
