'''
Created on Sep 30, 2014

@author: ds-ga-1007
'''
def main():
    first_name=raw_input("Enter your first name: ")
    last_name=raw_input("Enter your last name: ")
    print "Enter your date of birth: "
    month=raw_input("Month? ")
    day=raw_input("Day? ")
    year=raw_input("Year? ")
    print first_name+" "+last_name+" "+"was born on "+month+" "+str(day)+","+str(year)+"."
    
if __name__ == '__main__':
    main()