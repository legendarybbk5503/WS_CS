import math
import numpy

root5 = math.sqrt(5)
phi1 = (1+root5)/2
phi2 = (1-root5)/2

n = 1
while True:
    print(n)
    print(numpy.floor((numpy.power(phi1, n)-numpy.power(phi2, n))/root5))
    #print(math.floor((math.pow(phi1, n)-math.pow(phi2, n))/root5))
    n += 1  