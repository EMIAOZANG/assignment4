import sys
import os

if __name__=="__main__":

	v = [0]*5

	v[0] = (3*5)/(2+3)
	v[1] = (7+9)**0.5*2
	v[2] = (4-7)**3
	v[3] = (-19+100)**0.25
	v[4] = 6 % 4

	for i in range(5):
		print v[i]
