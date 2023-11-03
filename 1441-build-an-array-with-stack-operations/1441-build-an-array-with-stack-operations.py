class Solution:
    def buildArray(self, target, n) -> List[str]:
        i, curr = 0, 1
        final = []
        while i < len(target) and curr <= n:
            final.append("Push")
            if target[i] == curr:
                i += 1
            else:
                final.append("Pop")
            curr += 1 
        return final