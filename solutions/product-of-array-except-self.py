# O(n) time, "O(1)" space [aside from answer]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        left = 1
        for i in range(len(nums)):
            n = nums[i]
            res[i] *= left
            left *= n
        
        right = 1
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            res[i] *= right
            right *= n
        
        return res
