class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # Initialize left and right pointers.
        left, right = max(weights), sum(weights)

        # Perform binary search until left >= right.
        while left < right:

            # Calculate mid capacity and initialize variables.
            mid, need, cur = (left + right) // 2, 1, 0

            # Check if current weight exceeds the mid capacity.
            for w in weights:
                if cur + w > mid:
                    need += 1
                    cur = 0

                # Add package weight to current weight.
                cur += w

            # If number of days needed to transport all packages is greater than given days,
            # increase capacity by setting left = mid + 1. Otherwise, decrease capacity by setting right = mid.
            if need > days: 
                left = mid + 1
            else: 
                right = mid

        # Return left pointer as minimum capacity needed to transport all packages within given number of days.
        return left
        