class Solution:
    def bestClosingTime(self, customers: str) -> int:
        if len(set(customers)) == 1:
            if customers[0] == 'Y':
                return len(customers)
            else:
                return 0
            
        curr_penalty = penalty = customers.count('Y')
        res = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                curr_penalty -= 1
            else:
                curr_penalty += 1
                
            if curr_penalty < penalty:
                penalty = curr_penalty
                res = i
        
        if customers[0] == 'N' and res == 0:
            return 0
        
        return res+1
        