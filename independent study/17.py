def letterCount(x):
    db = {
        0: 0, #""
        1: 3,  #one
        2: 3,  #two
        3: 5,  #three
        4: 4,  #four
        5: 4,  #five
        6: 3,  #six
        7: 5,  #seven
        8: 5,  #eight
        9: 4,  #nine
        10: 3, #ten
        11: 6, #eleven
        12: 6, #twelve
        13: 8, #thirteen
        14: 8, #fourteen
        15: 7, #fifteen
        16: 7, #sixteen
        17: 9, #seventeen
        18: 8, #eighteen
        19: 8, #nineteen
        20: 6, #twenty
        30: 6, #thirty
        40: 5, #forty
        50: 5, #fifty
        60: 5, #sixty
        70: 7, #seventy
        80: 6, #eighty
        90: 6, #ninety
        100: 7, #hunderd
        1000: 8 #thousand
    }
    count = 0
    if x >= 1000:
        count += db[x//1000] + db[1000]
        x = x % 1000
    if x >= 100:
        count += db[x//100] + db[100]
        x = x % 100
        if x != 0: count += 3 #3 from "and"
    if x > 20:
        count += db[(x//10)*10] + db[x%10]
    elif x > 0: count += db[x]
    return count

def main():
    count = 0
    for i in range(1, 1001):
        count += letterCount(i)
    print(count)

if __name__ == "__main__":
    main()