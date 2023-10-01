class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals and newInterval:
            return [newInterval]
        
        for i in range(len(intervals)):
            if i == len(intervals) - 1 and newInterval[0] >= intervals[i][0]:
                intervals.insert(i+1, newInterval)
            elif i == 0 and newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
            elif i > 0 and intervals[i-1][0] <= newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
        
        print(intervals)
        result = []
        
        for start, end in intervals:
            if result and start <= result[-1][1]:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        
        return result
        
        