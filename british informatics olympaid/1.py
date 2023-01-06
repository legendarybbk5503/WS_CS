def find(a, c): #a+b->c
    a_num = ord(a) - 64
    c_num = ord(c) - 64 
    if c_num < a_num:
        c_num += 26
    b_num = c_num - a_num
    return chr(b_num + 64) 

def decrypt(string):
    string = list(string)
    for i in range(len(string)-1, 0, -1):
        string[i] = find(string[i-1], string[i])
    return "".join(string)

def main():
    print(decrypt("ESVNMCW"))

if __name__ == "__main__":
    main()