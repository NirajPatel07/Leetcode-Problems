class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1 + str2 == str2 + str1 is true, that means they have the same divisor
        # see example 1: "ABCABC" + "ABC" = "ABC" + "ABCABC"
        # if there is no such divisor, then return ""
        # otherwise, we can use gcd to find the lengths
        # the answer is either 
        # - str1[0 .. g] or 
        # - str2[0 .. g]
        # where g is the gcd of their length
        return "" if str1 + str2 != str2 + str1 else str1[:gcd(len(str1), len(str2))]