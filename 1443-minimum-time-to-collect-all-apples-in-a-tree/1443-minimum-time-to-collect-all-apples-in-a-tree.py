class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        subtree={}
        for i,j in edges:            
            if(i not in subtree):
                subtree[i]=[j]
            else:
                subtree[i].append(j)
            if(j not in subtree):
                subtree[j]=[i]
            else:
                subtree[j].append(i)
            
        print("subtree map:- ",subtree)
        time=0
        visited=set()
        def dfs(root):
            nonlocal time
            nonlocal visited
            if(root in visited):
                return False
            visited.add(root)           
            subtreeHasApple=False
            for k in subtree[root]:
                if(dfs(k)):        
                    
                    subtreeHasApple=True
            if(subtreeHasApple or hasApple[root]):
                time+=2
                print("+2 as apple found either (in subtree) or (at vertex itself) for node:",root)
                return True
            return False
            

        dfs(0)
        if(time>0):
            return time-2
        return time