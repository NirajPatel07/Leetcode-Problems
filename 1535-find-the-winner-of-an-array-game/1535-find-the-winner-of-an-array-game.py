class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        winner = arr[0]
        count = 0
        # max_n = max(arr)
        
        for i in range(1, len(arr)):
            if winner > arr[i]:
                count += 1
            else:
                winner = arr[i]
                count = 1
            
            if count == k:
                break
        
        return winner