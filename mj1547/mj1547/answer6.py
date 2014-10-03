'''

@author: jiminzi
'''
def answer6():
    first = raw_input("Enter your first name: ")
    last = raw_input("Enter your last name: ")
    print "Enter your date of birth: "
    month =raw_input('Month? ')
    day = raw_input('Day? ')
    Year = raw_input('Year? ')
    print first,last,"was born on",month,day,Year,"."
if __name__ == '__main__':
    answer6()