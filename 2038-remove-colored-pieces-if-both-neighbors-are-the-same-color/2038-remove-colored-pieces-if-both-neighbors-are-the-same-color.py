class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        a_count = 0
        b_count = 0
        clength = len(colors) - 1
        
        for i in range(1, clength):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                a_count += 1
                
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                b_count += 1
        
        if a_count > b_count:
            return True
        
        return False
        
                
            