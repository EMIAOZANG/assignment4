#This is the program for assignment 4_6

def main():
    firname = raw_input('Please enter your first name: ')
    lasname = raw_input('Please enter your last name: ')
    print "Please enter your date of birth :) "
    month = raw_input('Month: ')
    day = raw_input('Day: ')
    year = raw_input('Year: ')
    ans = firname+" "+lasname+" was born on "+month+" "+day+","+" "+year+"."
    print ans


if __name__ == '__main__':
    main()

