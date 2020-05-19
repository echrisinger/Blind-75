    def threeSum(self, nums: List[int]) -> List[List[int]]:
        seen_counts = defaultdict(lambda: 0)
        
        res = set()
        for i, val in enumerate(nums):
            if seen_counts[val] >= 2:
                continue
                
            for val1 in nums[i+1:]:
                other_val = -(val1+val)
                val_tup = tuple(sorted([val, val1, other_val]))
                if other_val in seen_counts and seen_counts[other_val] and val_tup not in res:
                    res.add(val_tup)
                    
            seen_counts[val] += 1

        return [
            list(tup)
            for tup in res
        ]

