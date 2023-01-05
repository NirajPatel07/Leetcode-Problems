class Solution(object):
    def findMinArrowShots(self, points):
        if not points:
            return 0
        points.sort(key=lambda p: p[1])
        arrows = 1

        comparision_y_to_check_if_overlapping = points[0][1]
        for x,y in points[1:]:
            if x > comparision_y_to_check_if_overlapping:
                arrows +=1
                comparision_y_to_check_if_overlapping = y

        return arrows