"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.



"""
## Hash Set:

def isValidSudoku1(board):
    N = 9

    # hash sets for record the states (rows, columns, box)
    rows = [set() for _ in range(N)]
    cols = [set() for _ in range(N)]
    boxes = [set() for _ in range(N)]

    for r in range(N):
        for c in range(N):
            val = board[r][c]
            print(val)

            if val == ".":
                continue

            if val in rows:          # here , rows is hashmap so if the value if for first time, its ok, for repetatio it goes for False...
                return False
            rows[r].add(val)

            if val in cols:
                return False
            cols[c].add(val)

            idx = (r//3) * 3 + c //3
            if val in boxes[idx]:
                return False
            boxes[idx].add(val)
            print("_+_+_+_+_")
    
    return True
    #  Time complexity  = O(N*N), Space complexity = O(N*N)


# Array Fixed Length

def isValidSudoku(board):
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
def isValidSudoku(board):
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


print(isValidSudoku(board))
