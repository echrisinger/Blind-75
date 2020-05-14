class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) <= 2:
            return max(nums)
        
        dp_table = [
            [0]*(len(nums)-1)
            for _ in range(2)
        ]
        # top row is not robbing the first house
        # bottom row is robboing first house
        
        # maximum assuming you don't rob house 0 up to index i
        # maximum assuming you do rob house 0 ...
        dp_table[0][0] = 0
        dp_table[0][1] = nums[1]
        
        dp_table[1][0] = nums[0]
        dp_table[1][1] = nums[0]
        
        for i in range(2, len(nums)-1):
            dp_table[0][i] = max(dp_table[0][i-2] + nums[i], dp_table[0][i-1])
            dp_table[1][i] = max(dp_table[1][i-2] + nums[i], dp_table[1][i-1])

        print(dp_table)
        rob_last_house = max(dp_table[0][-2] + nums[-1], dp_table[0][-1])
        rob_first_house = dp_table[1][-1]
        
        return max(rob_last_house, rob_first_house)
            
            
