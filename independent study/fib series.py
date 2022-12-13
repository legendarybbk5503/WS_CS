import sys
import decimal

sys.set_int_max_str_digits(1_000_000)

def fib(n):
    decimal.getcontext().prec = 20_000
    root5 = decimal.Decimal(5).sqrt()
    phi1 = (1+root5)/2
    phi2 = (1-root5)/2
    return round((phi1**n - phi2**n) / root5)
    

print(fib(100000))