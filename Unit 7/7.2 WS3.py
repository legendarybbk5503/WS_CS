def mergeList(list1: list, list2: list):
    a, b = list1, list2
    merge = []
    while len(a) != 0 or len(b) != 0:
        if len(a) == 0:
            merge.extend(b)
            break
        elif len(b) == 0:
            merge.extend(a)
            break
        elif a[0] < b[0]:
            merge.append(a[0])
            a.pop(0)
        else:
            merge.append(b[0])
            b.pop(0)
        print(a)
        print(b)
    return merge

def main():
    list1 = [2, 5, 15, 36, 47, 56, 59, 78, 156, 244, 268]
    list2 = [18, 39, 42, 43, 66, 69, 100]
    print(mergeList(list1, list2))

if __name__ == "__main__":
    main()