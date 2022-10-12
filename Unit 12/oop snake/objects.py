import turtle
import random

class snake:
    def __init__(self): #snake head
        self._snakeHead = turtle.Turtle()
        self.initialiseSnake()
    
    def initialiseSnake(self):
        self._snakeHead.speed(0)
        self._snakeHead.shape("square")
        self._snakeHead.color("black")
        self._snakeHead.penup()
        self._snakeHead.goto(0, 100)
        self._snakeHead._direction = "stop"
        self._snakeBody = []

    def update(self):
        self.move()

    #ensure snake cannot go back on itself
    #if is is heading down it cannot head up
    def go_up(self):
        if self._snakeHead._direction != "down":
            self._snakeHead._direction = "up"
    def go_down(self):
        if self._snakeHead._direction != "up":
            self._snakeHead._direction = "down"
    def go_right(self):
        if self._snakeHead._direction != "left":
            self._snakeHead._direction = "right"
    def go_left(self):
        if self._snakeHead._direction != "right":
            self._snakeHead._direction = "left"
    
    def move(self):
        for i in range(len(self._snakeBody)-1, 0, -1):
            #get previous (x, y)
            x = self._snakeBody[i-1].xcor()
            y = self._snakeBody[i-1].ycor()
            #move current body part to new location (closer to head)
            self._snakeBody[i].goto(x, y)
        
        if self._snakeBody != []: #if snakeBody exists
            x = self._snakeHead.xcor() #get (x, y)
            y = self._snakeHead.ycor()
            self._snakeBody[0].goto(x, y) #move the closest body to head pos

        if self._snakeHead._direction == "up":
            y = self._snakeHead.ycor()
            self._snakeHead.sety(y+20)
        elif self._snakeHead._direction == "down":
            y = self._snakeHead.ycor()
            self._snakeHead.sety(y-20)
        elif self._snakeHead._direction == "right":
            x = self._snakeHead.xcor()
            self._snakeHead.setx(x+20)
        elif self._snakeHead._direction == "left":
            x = self._snakeHead.xcor()
            self._snakeHead.setx(x-20)
    
    def grow(self):
        part = turtle.Turtle()
        part.speed(0)
        part.shape("square")
        part.color("green")
        part.penup()
        self._snakeBody.append(part)
    
    def headAndBodyCollCheck(self):
        for part in self._snakeBody:
            print(f"part: {part}")
            if part.distance(self._snakeHead) < 20:
                print("head and body collision")
                return True
    
    def snakeDie(self):
        self._snakeHead.goto(0,0)
        self._snakeHead._direction = "stop"
        for part in self._snakeBody:
            part.hideturtle()
        self._snakeBody = []


class food:
    def __init__(self):
        self._item = turtle.Turtle()
        self._item.speed(0)
        self._item.shape("circle")
        self._item.color("red")
        self._item.penup()
        self._item.shapesize(0.50, 0.50)
        self._item.goto(random.randint(-290, 290), random.randint(-290, 290))
        self._move = False
    
    def update(self):
        self.relocate()

    def setMove(self, decision):
        self._move = decision
    
    def relocate(self):
        if self._move == True:
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            self._item.goto(x, y)
            self.setMove(False)

