###############################
#                             #
#       Answer 7              #
# by Maya Rotmensch (mer567)  #
#                             #
###############################




li = [1,2,3,4,5,6,7,8,9]

#option 1:

temp =[li[0]]*4+[li[1]]*3+[li[2]]*5+[li[3]]*4

print "option 1 output",  temp


# option 2: a fancier though not necessarily shorter way

temp2 = li[:4]*4
temp2.remove(2)
temp2.append(3)
temp2.sort() 
print "option 2 output", temp2
