class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        # calculate prefixMins left and right of k based on offset
        min_left = {}
        min_right = {}
        lmin = nums[k]
        for offset in range(k+1): 
            lmin = min(lmin, nums[k - offset]) 
            min_left[lmin] = offset
        rmin = nums[k]
        for offset in range(len(nums) - k): 
            rmin = min(rmin, nums[k + offset]) 
            min_right[rmin] = offset
        
        # sort prefixMins 
        l_keys_sorted = sorted(min_left.keys()) 
        r_keys_sorted = sorted(min_right.keys())

        # iterate from smallest prefixMins to the largest 
        out = 0
        l, r = 0, 0 
        while l < len(l_keys_sorted) and r < len(r_keys_sorted): 
            curMin = min(l_keys_sorted[l], r_keys_sorted[r])
            width = min_left[l_keys_sorted[l]] + min_right[r_keys_sorted[r]] + 1 
            out = max(out, width * curMin)
            if l == len(l_keys_sorted) - 1: 
                r += 1
            elif r == len(r_keys_sorted) - 1: 
                l += 1
            else: 
                if l_keys_sorted[l] <= r_keys_sorted[r]: 
                    l += 1
                else: 
                    r += 1
        
        return out 