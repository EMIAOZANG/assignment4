import sys
import os

if __name__ == "__main__":
	a = [i for i in range(1, 10)]

	a = a[:1]*a[3] + a[1:2]*a[2] + a[2:3]*a[4] + a[3:4]*a[3]

	print a
