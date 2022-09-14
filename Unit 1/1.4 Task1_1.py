numbers = [1, 2, 3, 4, 5, 6]

reverse = []
total = 0

for i in range(0, len(numbers)):
    reverse.append(numbers[len(numbers)-1-i])
    total += numbers[i]

print(f"reverse: {reverse}")
print(f"total: {total}")
print(f"average: {total/len(numbers)}")