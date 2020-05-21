class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l = 0
        r = len(nums) - 1
        while l != r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            if nums[l] <= nums[mid]:
                ascending = l, max(l, mid-1)
                other = min(r, mid+1), r
            elif nums[mid] <= nums[r]:
                ascending = min(r, mid+1), r
                other = l, max(l, mid-1)
            
            asc_l, asc_r = ascending
            if nums[asc_l] <= target <= nums[asc_r]:
                l = asc_l
                r = asc_r
            else: # binary search on both ascending subarrays
                l, r = other
            
        return l if nums[l] == target else -1

