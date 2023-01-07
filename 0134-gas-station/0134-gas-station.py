class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):gas[i]-=cost[i]
        total,curc=sum(gas),0
        if total<0:return -1
        pos=0
        mxx=-1
        for i in range(len(gas)-1,-1,-1):
            curc+=gas[i]
            if (total-curc)<=curc and mxx<curc:curc=mxx;pos=i
        return pos