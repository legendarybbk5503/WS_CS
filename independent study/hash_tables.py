class HashTable:
    
    def __init__(self, items: list, slots: int, algorithm: str):
        self.__items = items
        self.__slots = slots
        self.__algor = algorithm #algorithm in ["mod", "mid", "fold"]
        self.__hash = None #hash table (list or dict)
    
    def __algorithm(self, item) -> int: #key
        item = sum(list(map(ord, list(str(item)))))
        if self.__algor == "mod":
            return item % self.__slots
        if self.__algor == "mid":
            x = str(item**2)
            if len(x) % 2 == 1: x = f"0{x}"
            x = int(x[len(x)//2-1:len(x)//2+1])
            return x % self.__slots
        if self.__algor == "fold":
            x = str(item)
            if len(x) % 2 == 1: x = f"0{x}"
            x = map(int, [x[i:i+2] for i in range(0, len(x), 2)])
            return sum(x) % self.__slots
    
    def hashList(self) -> list:
        hash = [None] * self.__slots
        for item in self.__items:
            mod = self.__algorithm(item)
            i = mod
            while True:
                if hash[i] is None or hash[i] == "null":
                    hash[i] = item
                    break
                i = (i+1) % self.__slots
                if i == mod:
                    raise Exception(f"stuck at {item}\n{hash}")
        self.__hash = hash
    
    def hashDict(self) -> dict:
        hash = {}
        for item in self.__items:
            mod = self.__algorithm(item)
            i = mod
            while True:
                if i not in hash.keys():
                    hash.update({i: item})
                    break
                if i in hash.keys():
                    if hash.get(i) == "null":
                        hash.update({i: item})
                        break
                i = (i+1) % self.__slots
                if i == mod:
                    raise Exception(f"stuck at {item}\n{hash}")
        self.__hash = dict(sorted(hash.items()))
    
    def search(self, item) -> int: #key
        mod = self.__algorithm(item)
        i = mod
        
        if type(self.__hash) == list:
            while True:
                if self.__hash[i] is None:
                    return None
                if self.__hash[i] == item:
                    return i, item
                i = (i+1) % self.__slots
                if i == mod:
                    return None

        elif type(self.__hash) == dict:
            while True:
                if i not in self.__hash.keys():
                    return None
                if self.__hash.get(i) == item:
                    return i, item
                i = (i+1) % self.__slots
                if i == mod:
                    return None
    
    def delete(self, item):
        x = self.search(item)
        if x is None:
            raise Exception("item not found")
        else:
            i, item = x
            if type(self.__hash) == list:
                self.__hash[i] = "null"
            elif type(self.__hash) == dict:
                self.__hash.update({i: "null"})
    
    def getHash(self) -> list | dict:
        return self.__hash


def main():
    x = HashTable([2828, 1361, 2461, "2aervt", "fdashae"], 17, "mid")
    x.hashList()
    print(x.getHash())
    print(x.search(2828))
    x.delete(2828)
    print(x.search(2828))
    
    x.hashDict()
    print(x.getHash())
    print(x.search(2828))
    x.delete(2828)
    print(x.search(2828))

if __name__ == "__main__":
    main()