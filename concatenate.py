import numpy

n, m, p = map(int, input().split())
myarray1 = (numpy.array([input().strip().split() for _ in range(n)], int))
myarray2 = (numpy.array([input().strip().split() for _ in range(m)], int))

print( numpy.concatenate((myarray1, myarray2), axis =0))
