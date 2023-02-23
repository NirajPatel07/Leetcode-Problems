import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Create two heaps to store the projects with minimum capital and maximum profit.
        maxProfit = []  # Heap for storing maximum profits
        minCapital = [(c, p) for c, p in zip(capital, profits)]  # Heap for storing minimum capital needed to start a project and its profit
        heapq.heapify(minCapital)  # Convert the capital-profits list to a heap based on minimum capital
        
        # For k projects, find the project with minimum capital and add its profit to the maximum profit heap.
        for i in range(k):
            while minCapital and minCapital[0][0] <= w:
                # Select the project with minimum capital and add its profit to the max profit heap.
                c, p = heapq.heappop(minCapital)
                heapq.heappush(maxProfit, -1 * p)  # Negative sign is used to create a max heap
                
            # Check if there are no more projects left or we don't have enough capital to start any more projects.
            if not maxProfit:
                break
                
            # Select the project with the maximum profit and add its profit to our current capital.
            w += -1 * heapq.heappop(maxProfit)  # Negative sign is used to retrieve the maximum profit from max heap
            
        # Return the final maximized capital.
        return w
