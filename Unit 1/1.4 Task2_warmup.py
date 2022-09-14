board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

#print(board[0][1])
#print(board[2][0])
#print(board[3][2])
#print(board[0][3])

for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j])