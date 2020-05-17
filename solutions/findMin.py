class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            if nums[start] <= nums[end]:
                return nums[start]
            
            mid = start + (end-start)//2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            
            if nums[mid] < nums[start]:
                end = mid-1
            else:
                start = mid+1
        
        raise 'Should not reach here'

