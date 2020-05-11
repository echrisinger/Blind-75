class Solution:
    # ideas:
    # start from each index and grow right. That way each index
    # only has to multiply by a single number O(n^2).
    
    # next idea:
    # instead of having to iterate over all of the lengths to the right,
    # just store the minimum & the maximum to the right, then if negative
    # choose the minimum, else choose maximum.
    # at an index, either choose to use the previous product (to the right), or lose it
    # if the current index is 0, then the next left index will always be 0 for the maximum or minimum.
    
    def maxProduct(self, nums: List[int]) -> int:
        min_product = float('inf')
        max_product = -float('inf')
        
        curr_min_product = 1
        curr_max_product = 1
        for i, n in enumerate(nums):
            options = [curr_max_product * n, curr_min_product * n, n]
            curr_min_product = min(options)
            curr_max_product = max(options)
            
            max_product = max(curr_max_product, max_product)
            min_product = min(curr_min_product, min_product)
            
        return max_product

