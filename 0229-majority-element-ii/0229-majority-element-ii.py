class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        count = Counter(nums)
        
        for k, v in count.items():
            if v > len(nums) // 3:
                result.append(k)
                
        return result