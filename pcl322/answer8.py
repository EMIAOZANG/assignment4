import sys
import os

if __name__ == "__main__":

	dic = {'first':[2, 1], 'second':[2, 3], 'third':[3,4]}

	#step a
	tmp = dic['first']
	dic['first'] = dic['third']
	dic['third'] = tmp

	#step b
	dic['third'].sort()

	#step c
	dic['fourth'] = dic['second']

	#step d
	dic.pop('second')

	print dic

