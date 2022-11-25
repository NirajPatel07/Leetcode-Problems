from typing import List


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        NSL = []
        NSR = []
        stack = []
        for i in range(len(arr)):
            while len(stack) > 0 and stack[-1][0] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                NSL.append(-1)
            else:
                NSL.append(stack[-1][1])
            stack.append((arr[i], i))
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while len(stack) > 0 and stack[-1][0] > arr[i]:
                stack.pop()
            if len(stack) == 0:
                NSR.append(len(arr))
            else:
                NSR.append(stack[-1][1])
            stack.append((arr[i], i))
        NSR = NSR[::-1]
        s = 0
        for i in range(len(arr)):
            a = i - NSL[i]
            b = NSR[i] - i
            s += a * b * arr[i]
        return s % 1000000007