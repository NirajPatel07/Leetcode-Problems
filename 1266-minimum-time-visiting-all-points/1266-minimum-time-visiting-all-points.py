class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = 0
        s = points[0]
        for i in points[1:]:
            l1 = abs(s[0] - i[0])
            l2 = abs(s[1] - i[1])
            h = min(l1, l2)
            n += h
            n += max(l1,l2) - h
            s = i
        return n