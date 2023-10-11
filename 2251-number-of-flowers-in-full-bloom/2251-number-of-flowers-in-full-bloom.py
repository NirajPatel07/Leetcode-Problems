class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        events = [(start, 0, 1) for start, _ in flowers]
        events.extend((end+1, 0, -1) for _, end in flowers)
        events.extend((t, 1, i) for i,t in enumerate(people))
        ans = [0]*len(people)
        num_flowers = 0
        for _, et, idx in sorted(events): 
            if et == 0:
                num_flowers += idx
            else:
                ans[idx] = num_flowers
        return ans