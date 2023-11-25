class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        prefix = list(accumulate(nums))

        for i in range(n):
            lsum = prefix[i] - nums[i]
            rsum = prefix[-1] - prefix[i]

            ltotal = nums[i] * i - lsum
            rtotal = rsum - nums[i] * (n - i - 1)

            res.append(ltotal + rtotal)

        return res