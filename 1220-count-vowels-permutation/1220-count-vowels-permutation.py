class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 1000000007

        # Initialize counts for each vowel for length 1
        a = 1
        e = 1
        i = 1
        o = 1
        u = 1

        # Iterate from length 1 to n - 1
        for length in range(1, n):
            # Calculate the next counts for each vowel based on the previous counts
            nexta = e
            nexte = (a + i) % MOD
            nexti = (a + e + o + u) % MOD
            nexto = (i + u) % MOD
            nextu = a

            # Update the counts with the newly calculated values for the next length
            a = nexta
            e = nexte
            i = nexti
            o = nexto
            u = nextu

        # Calculate the total count of valid strings for length n
        sum = (a + e + i + o + u) % MOD

        return int(sum)