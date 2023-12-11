class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)
        
        def binary_search(arr: List[int], left: int, right:int, target: int) -> int:
            while left <= right:
                mid = left + (right-left)//2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                elif arr[mid] == target:
                    left = mid + 1
                    
            return right
        
        i = 0
        while i < N:
            target = arr[i]
            index = binary_search(arr, i, N-1, target)
            
            if index - i + 1 > 0.25*N:
                return arr[i]
            
            i = index + 1