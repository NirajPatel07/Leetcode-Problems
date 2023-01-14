class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        hm = defaultdict(list)
        for i in range(len(s1)):
            hm[s1[i]].append(s2[i])
            hm[s2[i]].append(s1[i])

        def smallest(original):
            res = original
            visited = set()
            def s(c):
                nonlocal res, visited
                for el in hm[c]:
                    if el not in visited and el in hm:
                        visited.add(el)
                        res = min(res, el)
                        s(el)

                visited.add(c)

            s(original)
            return res

        cache = {}
        res = ''
        for c in baseStr:
            if c in cache:
                res += cache[c]
                continue
            
            cache[c] = smallest(c)
            res += cache[c]
        
        return res