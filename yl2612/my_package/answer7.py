'''
Created on Sep 30, 2014

@author: ds-ga-1007
'''
def main():
    li=[1,2,3,4,5,6,7,8,9]
    li=li[0:4]*4
    li.sort()
    li[7]=3
    print li
if __name__ == '__main__':
    main()
    