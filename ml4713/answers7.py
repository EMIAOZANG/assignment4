"""This is the answer for question 7"""


li=[1,2,3,4,5,6,7,8,9]
newli=li[0:4]
newli.extend(newli)
newli.extend(newli)
newli.sort()
newli.remove(2)
newli.insert(8,3)
print newli
