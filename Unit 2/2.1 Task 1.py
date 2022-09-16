while True:
    bags = int(input("Enter the number of bags: "))
    sweets = int(input("Enter the number of sweets: "))
    if sweets > bags:
        break
    print("The number of sweets must be larger than the number of bags")
if (sweets - bags) % 2 == 0:
	print("It's possible")
else:
	print("It's impossible")