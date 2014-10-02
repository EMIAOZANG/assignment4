"""This is the answers for question 6"""


print 'Enter your first name: '
firstname=raw_input()
print 'Enter your last name: '
lastname=raw_input()
print "Enter your date of birth: "
print "Month? "   
month=raw_input()
print "Day? "
day=raw_input()  #or we can use input()here but since we want to concatenate it with string later, raw_input() would be a better choice.
print "Year? "
year=raw_input()



print firstname+' '+lastname+' '+'was born on '+month+' '+day+', '+year+'.'







