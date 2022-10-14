import os 

class Leaderboard:
    def __init__(self, filename):
        self.__filename = ""
        try:
            tempFilename = os.path.join(os.path.dirname(__file__), filename)
            open(tempFilename, "r")
        except:
            print(f"{filename} doesn't exist")
        else:    
            self.__filename = tempFilename
    
    def __isFile(self): #check if there is a file 
        if self.__filename == "":
            print(f"no file")
        return self.__filename

    def __readList(self): #return a list for other functions
        with open(self.__filename, "r") as f:
            x = f.read()[:-1].split("; ")
            _list = [i.split(", ") for i in x]
        _list.sort(key = lambda x: x[-1], reverse = True)
        return _list
    def read(self, no = None): #return a user friendly printout
        if self.__isFile() == "": return
        _list = self.__readList()
        if no not in list(range(1, len(_list)+1)) and no != None: return "not postive integer"
        if no is None: no, output = len(_list), "Leaderboard" #none for full list
        else: output = f"Top {no} Leaderboard"                #x for top x
        for i in range(no):
            output += f"\n{_list[i][0]}: {_list[i][1]}"
        return output


def main():
    x = Leaderboard("leaderboard.txt")
    print(x.read())
    
if __name__ == "__main__":
    main()