from __future__ import division

def main():

    # equation 1: mod operation first, then summation
    eq1 = 46 + 100 % 73
    # equation 2: first add up two numbers, then do mod
    eq2 = (46 + 100) % 73

    print eq1
    print eq2

if __name__ == '__main__':
    main()
