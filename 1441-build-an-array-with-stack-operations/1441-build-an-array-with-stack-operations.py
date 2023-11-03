class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        i, stream = 0, 1
        result = []
        
        while i < len(target) and stream <= n:
            result.append('Push')
            if target[i] != stream:
                result.append('Pop')
            else:
                i += 1
            stream += 1
        
        return result
        