class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = [(0, height[0])]
        for i, n in enumerate(height):
            if n > left[-1][1]:
                left.append((i, n))
        
        right = [(len(height)-1, height[len(height)-1])]
        for i in range(len(height)-1, -1, -1):
            n = height[i]
            if right[-1][1] < n:
                right.append((i,n))
        
        max_volume = 0
        l_idx = 0
        r_idx = 0
        while l_idx < len(left) and r_idx < len(right):
            l_ptr, l_h = left[l_idx]
            r_ptr, r_h = right[r_idx]
            
            curr_volume = min(l_h, r_h) * (r_ptr - l_ptr)
            max_volume = max(curr_volume, max_volume)
            
            if r_idx == len(right)-1:
                l_idx += 1
            elif l_idx == len(left)-1:
                r_idx += 1
            elif l_h < r_h:
                l_idx += 1
            else:
                r_idx += 1
            
        return max_volume
    
# solution works in O(n) time, but O(n) space
# can be improved with just using two "sticky" pointers.
# IE, only move ptr inward if the other value adds more to the potential height
# of the container. The only point to moving inward is to find a container side
# of greater height, so we should always move the smaller of the two, as
# otherwise we will be bounding by the height of the smalles (& reducing width).
