import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create heaps for minimum capital and maximum profit projects.
        maxProfit = []  
        minCapital = [(c, p) for c, p in zip(capital, profits)]  
        heapq.heapify(minCapital)  
        
        # Find k projects with minimum capital and add their profit to the max profit heap.
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)  
            
            # If no more projects or insufficient capital to start a project, stop.
            if not maxProfit:
                break
                
            # Select project with maximum profit and add its profit to our capital.
            w += -1 * heapq.heappop(maxProfit)  
        
        # Return final maximized capital.
        return w
