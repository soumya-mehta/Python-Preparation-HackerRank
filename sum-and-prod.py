import numpy

n, m = map(int, input().split())

my_array = numpy.array([input().strip().split() for _ in range (n)], int)

arr1 = numpy.sum(my_array, axis = 0)
print(numpy.prod(arr1, axis = 0))
