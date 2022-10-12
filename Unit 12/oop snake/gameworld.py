from window import *
from objects import *
import time

height = width = 800

class Game:
    def __init__(self):
        self._window = window(width, height)
        self._snake = snake()
        self._food = food()

        self._playerScore = 0
        self._highScore = 0
    
    def keyboardListener(self):
        self._window._screen.listen()
        self._window._screen.onkey(self._snake.go_up, "Up")
        self._window._screen.onkey(self._snake.go_down, "Down")
        self._window._screen.onkey(self._snake.go_right, "Right")
        self._window._screen.onkey(self._snake.go_left, "Left")

    def worldUpdate(self):
        #check if snake head is within 15 pixels of food
        if self._snake._snakeHead.distance(self._food._item) < 15:
            self._food.setMove(True)
            self._playerScore += 10
            self._snake.grow()
        
        #wall
        left = width * -0.5
        right = width * 0.5
        top = height * 0.5
        bottom = height * -0.5

        condition1 = self._snake._snakeHead.xcor() > right
        condition2 = self._snake._snakeHead.xcor() < left
        condition3 = self._snake._snakeHead.ycor() > top
        condition4 = self._snake._snakeHead.ycor () < bottom

        if condition1 or condition2 or condition3 or condition4 or self._snake.headAndBodyCollCheck():
            time.sleep(1)
            self._snake.snakeDie()
            if self._playerScore > self._highScore:
                self._highScore = self._playerScore
            self._playerScore = 0
        
        self._window.drawHud(self._playerScore, self._highScore)


    def runGame(self): #game loop
        while True:
            self._window._screen.update()
            self.keyboardListener()

            self._snake.update()
            self._food.update()
            self.worldUpdate()

            time.sleep(0.1)


def main():
    game = Game()
    game.runGame()

if __name__ == "__main__":
    main()
