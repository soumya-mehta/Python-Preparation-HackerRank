import numpy

#first map both the entries in n and m respectively
n, m= map(int, input().split())

#form the array and removing any whitespaces between the elements given as input
myarray = numpy.array([input().strip().split() for _ in range(n)], int)

print(numpy.transpose(myarray))
print(myarray.flatten())
