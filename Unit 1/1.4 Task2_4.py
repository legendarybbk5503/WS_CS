outletSales = [
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [1, 2, 3, 4]
]
total = []

for i in range(len(outletSales[0])):
    sum = 0
    for j in range(len(outletSales)):
        sum += outletSales[j][i]
    total.append(sum)

print(total)

