slow = 0
medium = 0
fast = 0

while True:
    timeTaken = int(input("time taken: "))
    if timeTaken == 0:
        break
    elif timeTaken < 30:
        fast += 1
    elif timeTaken < 60:
        medium += 1
    else:
        slow += 1

print(f"fast: {fast}")
print(f"medium: {medium}")
print(f"slow: {slow}")