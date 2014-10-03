import sys
import os

if __name__ == "__main__":

	f = raw_input('Enter your first name: ')
	l = raw_input('Enter your last name: ')
	m = raw_input('Enter your date of birth\nMonth? ')
	d = raw_input('Day? ')
	y = raw_input('Year? ')
	
	print f + ' ' + l + ' was born on ' + m + ' ' + d + ' ' + y
