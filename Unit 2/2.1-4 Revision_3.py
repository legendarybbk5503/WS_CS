number = 0
while (number < 1) or (number > 10):
    number = int(input("Enter a positive whole number: "))
    if number > 10:
        print("Number too large.")
    elif number < 1:
        print("Not a postive number.")

c = 1
for k in range(number):
    print(c)
    c = (c * (number-1-k)) // (k+1)

