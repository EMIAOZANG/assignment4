def main():

    f_name = raw_input('Enter your first name: ')
    l_name = raw_input('Enter your last name: ')
    month = raw_input('Enter your date of birth:\nMonth? ')
    day = raw_input('Day? ')
    year = raw_input('Year? ')
    print '{0} {1} was born on {2} {3}, {4}.'.format(f_name, l_name, month, day, year)

if __name__ == '__main__':
    main()
