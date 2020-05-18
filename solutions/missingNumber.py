class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for n in range(0, len(nums)+1):
            res ^= n
        for n in nums:
            res ^= n
        return res


