number1 = int(input("Enter a whole number: "))
number2 = int(input("Enter another whole number: "))
temp1 = number1
temp2 = number2
while temp1 != temp2:
    if temp1 > temp2:
        temp1 = temp1 - temp2
    else:
        temp2 = temp2 - temp1
result = temp1
print(f"{result} is GCF of {number1} and {number2}")