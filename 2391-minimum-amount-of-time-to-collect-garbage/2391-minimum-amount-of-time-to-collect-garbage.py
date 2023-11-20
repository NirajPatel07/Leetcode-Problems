class Solution(object):
    def garbageCollection(self, garbage, travel):
        """
        :type garbage: List[str]
        :type travel: List[int]
        :rtype: int
        """
        count_garbage_by_name = {
            "G": 0,
            "P": 0,
            "M": 0,
        }
        total_minutes = 0
        for garbage_house, travel_to_house in reversed(list(zip(garbage, [0] + travel))):
            for garbage_name in garbage_house:
                count_garbage_by_name[garbage_name] += 1
            if travel_to_house > 0:
                total_minutes += travel_to_house * len([c for c in count_garbage_by_name.values() if c > 0])
        total_minutes += sum(count_garbage_by_name.values())
        return total_minutes