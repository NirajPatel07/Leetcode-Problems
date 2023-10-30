class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lookup = {}
        
        for n in arr:
            bit_count = bin(n).count('1')
            if bit_count in lookup:
                lookup[bit_count].append(n)
            else:
                lookup[bit_count] = [n]
        
        count_keys = sorted(lookup.keys())
        result = []
        
        for key in count_keys:
            curr_arr = lookup[key]
            curr_arr.sort()
            result.extend(curr_arr)
        
        return result