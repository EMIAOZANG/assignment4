if __name__ == '__main__':
    list = [1,2,3,4,5,6,7,8,9]
    ls = list[0:4] * 4
    ls.sort()
    ls[7] = 3
    print ls
