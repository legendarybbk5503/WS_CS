import turtle

class window:
    def __init__(self, width, height):
        self._screen = turtle.Screen()
        self._screen.title("OOP Snake")
        self._screen.bgcolor("blue")
        self._screen.setup(width, height)
        self._screen.tracer(0)