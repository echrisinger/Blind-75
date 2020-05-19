class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        
        res = [1]*len(nums)
        before = 1
        after = 1
        for i in range(1,len(nums)):
            after *= nums[len(nums)-i]
            before *= nums[i-1]
            res[i] *= before
            res[len(nums)-1-i] *= after
            
        return res
# O(n) runtime, O(1) complexity

