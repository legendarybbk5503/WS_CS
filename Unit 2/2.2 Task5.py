def initialise():
    print("This program finds the maxiumums of sets of three numbers.")
    print("Entre three zeros when all numbers entered.")
    print("Program then calculates and outputs the average of the maximums.")
    global total, n
    total = 0
    n = 0

def promptForNumbers():
    global num1, num2, num3
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter the second number: "))
    num3 = int(input("Please enter the third number: "))

def findMax():
    global maxnum
    maxnum = num1
    if num2 > maxnum: maxnum = num2
    if num3 > maxnum: maxnum = num3
    print(f"Max of the three numbers is {maxnum}")

def performCalculations():
    global total, n
    total += maxnum
    n += 1

def processData():
    promptForNumbers()
    while num1 != 0 and num2 != 0 and num3 != 0:
        findMax()
        performCalculations()
        promptForNumbers()

def calculateAverage():
    average = total / n
    print(f"Average of maximums is {average}")

def main():
    initialise()
    processData()
    calculateAverage()

main()
