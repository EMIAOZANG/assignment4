'''
Created on Sep 29, 2014

@author: ds-ga-1007


'''
def main():
    li1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    li2 = li1[:4] * 4
    li2.sort()
    li2[7] = 3
    print li2
    
if __name__ == '__main__':
    main()
