class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result = []
        groups = {}
        
        for row in range(len(nums)-1, -1, -1):
            for column in range(len(nums[row])-1, -1, -1):
                diagonal = row + column
                if diagonal in groups:
                    groups[diagonal].append(nums[row][column])
                else:
                    groups[diagonal] = [nums[row][column]]
        
        curr = 0
        while curr in groups:
            result.extend(groups[curr])
            curr += 1
        
        return result