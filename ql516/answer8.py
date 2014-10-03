'''
Created on Sep 30, 2014

@author: ql516
'''
##a
dic = {'first':[2,1],'second':[2,3],'third':[3,4]};
tmp=dic['first'];
dic['first']=dic['third'];
dic['third']=tmp;

##b
dic['third'].sort();

##c
dic['fourth']=dic['second'];

##d
del dic['second'];


print dic