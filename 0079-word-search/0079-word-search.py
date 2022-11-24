class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m = len(board)
        n = len(board[0])
        p = len(word)
        
        if m*n < p:
            return False
        
        board_set = set(board[i][j] for i in range(m) for j in range(n))
        word_set = set(c for c in word)
        if len(board_set) < len(word_set):
            return False
        
        
        def check_char(i, j, k, resting):
            if k >= p:
                return True
            
            if p-1-k > resting:
                return False
            
            if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == word[k]:
                board[i][j] = None
                directions = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                if any(check_char(ii, jj, k+1, resting-1) for ii, jj in directions):
                    return True
                board[i][j] = word[k]
                
            return False
                
        
        for i in range(m):
            for j in range(n):
                if check_char(i, j, 0, m*n):
                    return True
                
        return False