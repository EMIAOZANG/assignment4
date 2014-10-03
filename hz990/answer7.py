a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Here is the transformation
b = a[:4]*4
b.sort()
b[7] = 3

print b