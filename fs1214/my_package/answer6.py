'''
Created on Sep 29, 2014

@author: ds-ga-1007


'''
def main():
    fname = raw_input("Enter your first name: ")
    lname = raw_input("Enter your last name: ")
    print "Enter your date of birth:"
    month = raw_input("Month? ")
    day = input("Day? ")
    year = input("Year? ")
    print "{} {} was born on {} {},{}.".format(fname, lname, month, day, year)

if __name__ == '__main__':
    main()