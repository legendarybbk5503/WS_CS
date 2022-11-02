from random import randint

class DiceGame:
    def __init__(self, a, b):
        if not self.__authorised(a, b): return
        self.__player = [a, b]
    
    def __authorised(self, a, b):
        authorisedList = ["a", "b"]
        if a not in authorisedList and b not in authorisedList: print(f"both {a} and {b} are not authorised")
        elif a not in authorisedList: print(f"{a} is not authorised")
        elif b not in authorisedList: print(f"{b} is not authorised")
        else:
            print(f"{a} and {b} are authorised")
            return True 
        return False
    
    def __roll(self):
        score = [0, 0]
        rollList = [randint(1, 6) for _ in range(4)]
        for i in range(2):
            print(f"{self.__player[i]} rolled {rollList[i*2]} and {rollList[i*2+1]}")
            sum = rollList[i*2]+rollList[i*2+1]
            score[i] += sum
            if sum % 2 == 0: score[i] += 10
            else: score[i] -= 5
            if rollList[i*2] == rollList[i*2+1]:
                extra = randint(1, 6)
                score[i] += extra
                print(f"It's a double, {self.__player[i]} rolled a {extra}")
        return score[0], score[1]
    
    def startGame(self):
        score = [0, 0]
        round = 1
        while round <= 5:
            print(f"Round {round}")
            temp = self.__roll()
            score = [score[i] + temp[i] for i in range(2)]
            for i in range(2):
                if score[i] < 0: score[i] = 0
                print(f"{self.__player[i]} score: {score[i]}")
            round += 1
        while score[0] == score[1]:
            for i in range(2):
                _1DiceRoll = randint(1, 6)
                print(f"{self.__player[i]} rolled a {_1DiceRoll}")
                score[i] += _1DiceRoll
                if _1DiceRoll % 2 == 0: score[i] += 10
                else: score[i] -= 5
            for i in range(2):
                if score[i] < 0: score[i] = 0
                print(f"{self.__player[i]} score: {score[i]}")
        if score[0] > score[1]: print(f"{self.__player[0]} won")
        else: print(f"{self.__player[1]} won")

def main():
    game = DiceGame("a", "b")
    game.startGame()

if __name__ == "__main__":
    main()
