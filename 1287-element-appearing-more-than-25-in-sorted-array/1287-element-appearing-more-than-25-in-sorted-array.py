class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        res = arr[0]
        count = 1
        percentage = len(arr)//4
        
        for num in arr[1:]:
            if num == res:
                count += 1
            else:
                res = num
                count = 1
            
            if count > percentage:
                return num
        
        return res