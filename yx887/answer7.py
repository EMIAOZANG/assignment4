def main():
    
    # create the starting list
    start = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # transform towards final list
    b = start[:4] * 4
    b.sort()
    b[7] = 3
    
    # if * operation is not allowed, we can do this inplace
    b = start[:4]
    b.extend([1,1,1,2,2,3,3,3,3,4,4,4])
    b.sort()

    # print the final list
    print b

if __name__ == '__main__':
    main()
