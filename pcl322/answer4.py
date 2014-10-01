import sys
import os
import numpy

if __name__=="__main__":

	v = [0]*5

	v[0] = (3*5)/(2+3)
	v[1] = numpy.sqrt(7+9)*2
	v[2] = numpy.power(4-7, 3)
	v[3] = numpy.power(-19+100, 0.25)
	v[4] = 6 % 4

	for i in range(5):
		print v[i]
