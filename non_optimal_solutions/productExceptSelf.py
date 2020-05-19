class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        before, after = [1]*len(nums), [1]*len(nums)
        for i in range(len(nums)-1):
            before[i+1] = before[i]*nums[i]
            rev_i = len(nums) - 1 - i
            after[rev_i-1] = after[rev_i] * nums[rev_i]
            
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = before[i] * after[i]
            
        return res
# O(n) space

