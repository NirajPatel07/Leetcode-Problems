class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        result = []
        maxCount = max(count.values())
        
        for i in range(maxCount):
            temp = []
            for key, value in count.items():
                if count[key] >= 1:
                    count[key] -= 1
                    temp.append(key)
            result.append(temp)
        
        return result
            