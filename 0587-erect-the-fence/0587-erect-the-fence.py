class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        

        def check_clockwise(p1,p2,p3):
            
            x1,y1 = p1
            x2,y2 = p2
            x3,y3 = p3
            """
            slope of p1 and p2 will be y2-y1/x2-x1
            
            slope of p2 and p3 will be y3-y2/x3-x2
            
            combining them both gives
            
            y3-y2/x3-x2   -   y2-y1/x2-x1 
            
            this eqn represents the resultant formed by those two
            if this is greater than 0 then direction will be counter clockwise else clockwise
            """
            return (y3-y2)*(x2-x1)-(y2-y1)*(x3-x2) #return <0 if clockwise
        
        
        trees.sort()
        upper = []
        lower = []
        
        for t in trees:
            
            while len(upper)>1 and check_clockwise(upper[-1],upper[-2],t)>0:
                upper.pop()
            
            while len(lower)>1 and check_clockwise(lower[-1],lower[-2],t)<0:
                lower.pop()
            
            upper.append(tuple(t))
            lower.append(tuple(t))
        
        return list(set(upper+lower))