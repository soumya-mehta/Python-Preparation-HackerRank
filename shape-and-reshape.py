import numpy

#make an array with input values splitting them into individual elements in integer formal
myarray = numpy.array(input().split(),int)

#reshape the array to have dimensions 3x3
myarray = numpy.array(myarray).reshape(3,3)

#print the array
print(myarray)
