# time & space O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for i, n in enumerate(nums):
            other = target - n
            if other in previous:
                return [previous[other], i]
            
            previous[n] = i
            
        raise Exception("pizza")

