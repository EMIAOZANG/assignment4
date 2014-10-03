dic = {'first':[2,1], 'second':[2,3], 'third':[3,4]}
swap = dic['first']
dic['first']=dic['third']
dic['third']=swap
dic['third'].sort()
dic['fourth']=dic['second']
del dic['second']
print dic
