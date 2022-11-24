def evenSum(n: int):
    if n > 0:
        if n%2 == 1: return evenSum(n-1)
        else: return n + evenSum(n-2)
    else: return n

print(evenSum(11))