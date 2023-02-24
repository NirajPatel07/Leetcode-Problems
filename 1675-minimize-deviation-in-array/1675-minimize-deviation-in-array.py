class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # initialize a heap data structure to store the transformed values of the array elements
        heap = []
        for num in nums:
            # transform the number to an odd number if it is odd
            transformed_num = num
            while transformed_num % 2 == 0:
                transformed_num //= 2
            # append the tuple (transformed number, maximum limit) to the heap
            heap.append((transformed_num, max(num, transformed_num*2)))
        
        # find the maximum value in the heap
        max_num = max(i for i,j in heap)
        # convert the list to a heap data structure
        heapify(heap)
        # initialize the minimum deviation to be a large value
        min_deviation = float("inf")

        # loop until all the elements in the heap have been processed
        while len(heap) == len(nums):
            # pop the smallest element from the heap
            num, limit = heappop(heap)
            # update the minimum deviation
            min_deviation = min(min_deviation, max_num - num)
            # if the popped element can be doubled and still be within its limit, then push it back to the heap with the doubled value
            if num < limit:
                heappush(heap, (num*2, limit))
                max_num = max(max_num, num*2)
            
        # return the minimum deviation
        return min_deviation
