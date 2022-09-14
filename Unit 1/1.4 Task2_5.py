def reset():
    global grid
    grid = [
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
        ['x', 'x', 'x', 'x'],
    ]

def move(i, j):
    grid[i][j] = 'O'

def output():
    for i in range(len(grid)):
        x = ""
        for j in range(len(grid[0])):
            x += f"{grid[i][j]} "
        print(x)

def main():     
    reset()
    move(0, 0)
    output()
    while True:
        _input = input("Type Coordinates: ")
        i = int(_input[:_input.find(",")]) - 1
        j = int(_input[_input.find(",")+1:]) - 1
        reset()
        move(i, j)
        output()

main()