#the following codes are used to show prompts to instruct users inputing their names and date of birth and store them in variables

f_name = raw_input('Enter your first name: ')
l_name = raw_input('Enter your last name: ')
month = raw_input('Enter your date of birth:\nMonth? ')
day = input('Day? ')
year = input('Year? ')
format_str = '%s %s was born on %s %d, %d' %(f_name,l_name,month,day,year)
print format_str