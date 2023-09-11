class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        
        for i in range(len(groupSizes)):
            if groupSizes[i] in groups:
                if len(groups[groupSizes[i]][0]) < groupSizes[i]:
                    groups[groupSizes[i]][0].append(i)
                else:
                    flag = True
                    for arr in groups[groupSizes[i]]:
                        if len(arr) < groupSizes[i]:
                            arr.append(i)
                            flag = False
                    
                    if flag:
                        groups[groupSizes[i]].append([i])
            else:
                groups[groupSizes[i]] = [[i]]
                
        res = []
        
        for key, value in groups.items():
            res.extend(value)
        
        return res