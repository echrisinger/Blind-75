class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0
        start = 0
        for i, val in enumerate(nums):
            # 4 -1 2 1 -5 4
            curr_sum += val 
            if curr_sum < val:
                start = i
                curr_sum = val
            
            max_sum = max(curr_sum, max_sum)
            
        return max_sum

