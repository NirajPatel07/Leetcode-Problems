class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        # initialize pointers i and j to end of a and b respectively
        i, j = len(a) - 1, len(b) - 1
        carry = 0  # initialize carry to 0
        while i >= 0 or j >= 0:
            # add carry to the sum of a[i] and b[j] (if they exist)
            sum_ = carry
            if i >= 0:
                sum_ += ord(a[i]) - ord('0')
            if j >= 0:
                sum_ += ord(b[j]) - ord('0')
            i, j = i - 1, j - 1  # move the pointers to the next digit
            carry = 1 if sum_ > 1 else 0  # update carry based on sum
            res += str(sum_ % 2)  # append the binary digit to result string
        if carry != 0:
            res += str(carry)  # append carry to result string if it exists
        return res[::-1]  # reverse and return the result string
