def sudoku(puzzle):
    def trial(i, j):
        trial_list = []
        row = puzzle[i]
        column = [puzzle[x][j] for x in range(0, 9)]
        sq_i, sq_j = i//3, j//3
        square = []
        for x in range(3):
            for y in range(3):
                square.append(puzzle[sq_i*3+x][sq_j*3+y])

        for trial in range(1, 10):
            con1 = trial in row
            con2 = trial in column
            con3 = trial in square
            if not(con1 or con2 or con3):
                trial_list.append(trial)
        return trial_list
    
    #trial(7, 7)

    while True:
        for i in range(9):
            for j in range(9):
                if 0 not in puzzle[i]: break
                if puzzle[i][j] == 0:
                    trial_list = trial(i, j)
                    #print(trial_list)
                    if len(trial_list) == 1:
                        puzzle[i][j] = trial_list[0]
                        for x in puzzle: print(x)
                        print("\n")
        count = 0
        for _list in puzzle:
            count += _list.count(0)
        if count == 0: break


    """return the solved puzzle as a 2d array of 9 x 9"""
    return puzzle

puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

def main():
    sudoku(puzzle)

main()