'''
Created on Sep 30, 2014

@author: ds-ga-1007
'''
def main():
    li=[1,2,3,4,5,6,7,8,9]
    li1=[li[0]]*4+[li[1]]*3+[li[2]]*5+[li[3]]*4
    print li1
    # method2
    li2=li[:4]*4
    li2.sort()
    li2[7]=3
    print li2 
    #  method3
    li3=li[:4]
    li3.extend([1,1,1,2,2,3,3,3,3,4,4,4])
    li3.sort()
    print li3 
if __name__ == '__main__':
    main()
    