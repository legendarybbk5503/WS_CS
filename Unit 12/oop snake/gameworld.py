from window import *
from objects import *
import time

height = width = 800

class Game:
    def __init__(self):
        self._window = window(width, height)
        self._snake = snake()
        self._food = food()
    
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
            self._snake.grow()
        
        #walls
        left = width * -0.5
        right = width * 0.5
        top = height * 0.5
        bottom = height * -0.5

        condition1 = self._snake._snakeHead.xocr() > right
        condition2 = self._snake._snakeHead.xocr() < left
        condition3 = self._snake._snakeHead.yocr() > top
        condition4 = self._snake._snakeHead.yocr() < bottom

        if condition1 or condition2 or condition3 or condition4:
            time.sleep(1)
            self._snake._snakeHead.goto(0,0)            #back to origin
            self._snake._snakeHead._direction = "stop"  #stay until next key press
            self._snake.clearBody()                     #clear body


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
