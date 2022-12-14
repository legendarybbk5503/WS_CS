import math
import decimal

root5 = decimal.Decimal(5).sqrt()
phi1 = (1+root5)/2
phi2 = (1-root5)/2

n = 1
while True:
    print(n)
    print(math.floor((math.pow(phi1, n)-math.pow(phi2, n))/root5))
    n += 1  

