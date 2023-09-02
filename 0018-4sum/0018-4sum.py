class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        nums.sort()
        
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                left = j+1
                right = len(nums)-1
                while left<right:
                    curr = nums[i]+nums[j]+nums[left]+nums[right]
                    if curr == target:
                        res.add((nums[i], nums[j], nums[left], nums[right]))
                        left+=1
                        right-=1
                    elif curr>target:
                        right-=1
                    else:
                        left+=1
        return res