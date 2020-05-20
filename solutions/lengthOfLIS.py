class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        sequences = {
            1: nums[0]
        }
        max_length_sequence = 1
        for n in nums[1:]:
            if n > sequences[max_length_sequence]:
                max_length_sequence += 1
                sequences[max_length_sequence] = n
            else:
                length = max_length_sequence
                for length in range(max_length_sequence, 0, -1):
                    if (length == 1) or n > sequences[length-1]:
                        sequences[length] = min(sequences[length], n)
        
        return max_length_sequence

# O(n^2) time and space
