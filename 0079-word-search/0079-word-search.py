class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        path = set()
        
        def search_word(r, c, idx):
            if idx == len(word):
                return True
            
            if (r<0 or c<0 or r>=row or c>=col or (r, c) in path or board[r][c] != word[idx]):
                return False
            
            path.add((r,c))
            res = (
                search_word(r+1, c, idx+1) or
                search_word(r, c+1, idx+1) or
                search_word(r-1, c, idx+1) or
                search_word(r, c-1, idx+1)
                  )
            path.remove((r,c))
            
            return res
        
        for r in range(row):
            for c in range(col):
                if search_word(r, c, 0):
                    return True
                
        return False