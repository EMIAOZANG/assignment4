import os

if __name__ == "__main__":

    a = [1,2,3,4,5,6,7,8,9]

    b = a[:4]*4
    b.sort()
    b[7] = 3

    print b

"""
 there's another method that needs shorter statements but I'm not sure if it satisfies the requirement. So I'm only showing it here

    b = [a[0]]*4+[a[1]]*3+[a[2]]*5+[a[3]]*4
 
    print b
"""
