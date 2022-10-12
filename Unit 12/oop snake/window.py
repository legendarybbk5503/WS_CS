import turtle

class window:
    def __init__(self, width, height):
        self._screen = turtle.Screen()
        self._screen.title("OOP Snake")
        self._screen.bgcolor("blue")
        self._screen.setup(width, height)
        self._screen.tracer(0)
    
        self._hud = turtle.Turtle()
    
    def drawHud(self, score, highScore):
        self._hud.clear()
        self._hud.color("white")
        self._hud.penup()
        self._hud.hideturtle()
        self._hud.goto(0, -400)
        self._hud.write(f"Score: {score} High Score: {highScore}", align = "center", font = ("Courier", 22, "normal"))