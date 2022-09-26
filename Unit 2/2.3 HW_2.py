import random

barcodes = []
for _ in range(100):
    barcodes.append(str(random.randint(100000, 999999)))

#real code start
for i in range(len(barcodes)):
    sum = int(barcodes[i][0]) + int(barcodes[i][2]) + int(barcodes[i][4]) + (int(barcodes[i][1]) + int(barcodes[i][3]))*3
    if sum % 10 == int(barcodes[i][-1]): print(f"{barcodes[i]} is valid")
    else: print(f"{barcodes[i]} is invalid")