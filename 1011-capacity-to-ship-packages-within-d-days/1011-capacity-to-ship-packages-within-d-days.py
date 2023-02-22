class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def calculate_min(max_weight):
            days_count = 0
            curr_sum = 0
            for i in weights:
                if curr_sum + i <= max_weight:
                    curr_sum += i
                else:
                    curr_sum = i
                    days_count += 1
                    
            return days_count+1
        
        
        low = max(weights)
        high = sum(weights)
        
        if len(weights) == days:
            return low
        if days == 1:
            return high
        
        minimum_weights = high
        
        while low <= high:
            mid = (low+high)//2
            min_days = calculate_min(mid)
            if min_days <= days:
                minimum_weights = min(minimum_weights, mid)
                high = mid - 1
            else:
                low = mid + 1
        return minimum_weights
        
        