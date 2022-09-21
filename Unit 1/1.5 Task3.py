def getPword(attempt): #value of 1 or 2
    if attempt == 1:   print("enter password:")
    elif attempt == 2: print("enter password again:")
    pwd = input()
    return pwd

def main():
    while True:
        pwd = getPword(1)
        if len(pwd) in [6, 7, 8]:
            newpwd = getPword(2)
            if pwd == newpwd:
                print("Password change successful")
                break
            else:
                print("Error - passwords do not match")
        else:
            print("Error. Password must be 6 to 8 characters long")
    
main()