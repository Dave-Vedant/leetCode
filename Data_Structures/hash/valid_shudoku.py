"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.



"""
## Hash Set:
from collections import defaultdict
def isValidSudoku(board):
    N = 9      # hard coding the value as we know

    # hash sets for record the states (rows, columns, box)
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)    # (r/3, c/3), will give index of box ([0,1,2]by[0,1,2])

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            if val == ".":
                continue

            if (val in rows[r]) or (val in cols[c]) or (val in boxes[(r//3, c//3)]):  # in python x//y wil give integer (floor value)
                return False
            
            cols[c].add(val)
            rows[r].add(val)
            boxes[(r//3, c//3)].add(val)

    return True
    #  Time complexity  = O(N^2), Space complexity = O(N^2) = here, N=9.


# Array Fixed Length

def isValidSudoku1(board):
    N = 9

    rows = [[0] * N for _ in range(N)]          # [0,0,0,0,0,0,0,0]
    cols = [[0] * N for _ in range(N)]
    boxes = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):

            if board[r][c] == ".":
                continue

            pos = int(board[r][c]) - 1           # dealing with array...
            print(pos)
            if rows[r][pos] == 1:           # if the zero array has 1 on the row position, means that element repeat, means False
                return False
            rows[r][pos] = 1
            print(rows)


            if cols[c][pos] == 1:
                return False
            cols[c][pos] = 1
            print(cols)

            idx = (r//3) * 3 + c//3
            if boxes[idx][pos] == 1:
                return False
            boxes[idx][pos] = 1
            print("looooooop")
    return True
    # time complexity = O(N^2), space complexity = O(N^2)


## Bit Masking:
def isValidSudoku2(board):
    N = 9

    rows = [0] * N
    cols = [0] * N
    boxes = [0] * N

    for r in range(N):
        for c in range(N):
            if board[r][c] == ".":
                continue

            pos = int(board[r][c]) -1

            if rows[r] & (1<< pos):
                return False
            rows[r] |= (1<<pos)

            if cols[c] & (1<<pos):
                return False
            cols[c] |= (1<<pos)
        
            idx = (r//3) *3 + c//3
            if boxes[idx] & (1<<pos):
                return False
            boxes[idx]  |= (1<<pos)
    
    return True

    # time complexity = O(N^2), space complexity = O(N)




# execution:
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

board1 = [[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
print(isValidSudoku(board1))
