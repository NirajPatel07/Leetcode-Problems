from collections import Counter
class Solution:
    def maxPoints(self, points):
        points.sort()
        maximum = 0
        n = len(points)
        for i in range(n):
            slopes = []
            for j in range(i+1,n):
                if (points[j][0] - points[i][0]) == 0:
                    slopes.append("NO")
                else:
                    slopes.append((points[j][1] - points[i][1]) / (points[j][0] - points[i][0]))
            if len(slopes) > 0:
                test_list = Counter(slopes)
                res = test_list.most_common(1)[0][1]
                if res > maximum:
                    maximum = res


                

        return maximum +1