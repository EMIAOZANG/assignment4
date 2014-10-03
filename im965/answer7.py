#answer7.py
#im965 program for assignment 04, question 07

#!/usr/bin/env python

#operate on a list to get the desired final list

#set given list as l
l = [1,2,3,4,5,6,7,8,9]

#operations
l[1:9]=[1,1,1,2,2,2,3,3]
e=[3,3,3,4,4,4,4]
l.extend(e)

#display
print l
