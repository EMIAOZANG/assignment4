#This program is for assignment4_7

def main():
    a = [1,2,3,4,5,6,7,8,9]
    b = a[:4] * 4
    b.sort()
    b[7]=3

    print b
    


if __name__ == '__main__':
    main()

