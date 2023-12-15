class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set()
        
        for path in paths:
            seen.add(path[0])
        
        for path in paths:
            if path[1] not in seen:
                return path[1]