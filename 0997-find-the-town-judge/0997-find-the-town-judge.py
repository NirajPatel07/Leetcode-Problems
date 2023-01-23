class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_lookup = [0]*(n + 1)
        judge = 1
        max_trust = 0

        for i, j in trust:
            trust_lookup[i] -= 1
            trust_lookup[j] += 1

            if trust_lookup[j] > max_trust:
                judge = j
                max_trust = trust_lookup[j]

        return -1 if min(max_trust, trust_lookup[judge]) != n - 1 else judge