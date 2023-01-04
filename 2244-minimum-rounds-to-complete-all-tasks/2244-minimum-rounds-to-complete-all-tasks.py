from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ct=0
        dic=Counter(tasks)
        for x in dic:
            if dic[x]<=1:
                return -1
            elif dic[x]%3==0:
                ct+=dic[x]//3
            else:
                ct+=(dic[x]//3)+1
        return ct