class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, n in enumerate(nums):
            other = target-n
            if other in prev:
                return [prev[other], i]
            
            prev[n] = i
        
        raise

# O(n) time space
