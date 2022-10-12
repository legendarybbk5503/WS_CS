def main():
    _list = [1, 2]
    sum = 2
    while True:
        next = _list[len(_list)-1]+_list[len(_list)-2]
        if next > 4000000: break
        else:
            if next%2 == 0: sum += next
            _list.append(next)
    print(sum)

if __name__ == "__main__":
    main()