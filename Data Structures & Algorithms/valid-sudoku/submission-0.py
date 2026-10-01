class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in row:
                        print(1)
                        return False
                    else:
                        row.add(board[i][j])
            row.clear()

        col = set()
        for c in range(9):
            for r in range(9):
                if board[r][c] != ".":
                    if board[r][c] in col:
                        print(2)
                        return False
                    else:
                        col.add(board[r][c])
            col.clear()

        box1 = set()
        box2 = set()
        box3 = set()
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    if c < 3:
                        if board[r][c] in box1:
                            print(3)
                            return False
                        else:
                            box1.add(board[r][c])
                    elif c < 6:
                        if board[r][c] in box2:
                            print(4)
                            return False
                        else:
                            box2.add(board[r][c])
                    else:
                        if board[r][c] in box3:
                            print(5)
                            return False
                        else:
                            box3.add(board[r][c])
            if r == 2 or r == 5:
                box1.clear()
                box2.clear()
                box3.clear()

        return True
        

