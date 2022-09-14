maxAge = 0
ageList = []

for index in range(0, 4):
    ageList.append(int(input("Enter an age: ")))
    if ageList[index] > maxAge:
        maxAge = ageList[index]
        position = index

print(ageList[position], position)