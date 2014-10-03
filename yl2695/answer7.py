import sys


def main():    
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    a_final = a[:4] * 4
    a_final.sort()
    a_final[7] = 3
    print a_final
if __name__ == '__main__':
    main()
