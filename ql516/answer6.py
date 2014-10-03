'''
Created on Sep 30, 2014

@author: ql516
'''


firstname = raw_input("Enter your first name: ");

lastname = raw_input("Enter your last name: ");

print "Enter your date of birth: ";
d_m=raw_input("Month? ");

d_d=raw_input("Day? ");

d_y=raw_input("Year? ");

sent=firstname+" "+lastname+" was born on "+d_m+" "+d_d+", "+d_y+'.';
print sent;



