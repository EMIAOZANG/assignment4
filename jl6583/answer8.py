#initializing the dictionary
dic = {'first':[2,1],'second':[2,3],'third':[3,4]}
#a
temp = dic['first']
dic['first'] = dic['third']
dic['third'] = temp

#b
dic['third'].sort()

#c
dic['fourth'] = dic['second']

#d
dic.pop('second')

print dic