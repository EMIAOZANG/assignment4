def main():
    
    # create the starting list
    start = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # transform towards final list
    b = start[:4] * 4
    b.sort()
    b[7] = 3

    # print the final list
    print b

if __name__ == '__main__':
    main()
