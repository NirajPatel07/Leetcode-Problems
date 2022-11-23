class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for y in range(len(board)):
            t=[x for x in board[y] if x != "."]
            if len(set(t))!=len(t): return False
        #check colnums
        for x in range(len(board[0])):
            t=[row[x] for row in board if row[x] != "."]
            if len(set(t))!=len(t): return False
        #check squares
        for y in range(0,9,3):
            for x in range(0,9,3):
                t=[board[r][i] for r in range(y,y+3) for i in range(x,x+3) if board[r][i] !="."]
                if len(t)!=len(set(t)): return False
        return True