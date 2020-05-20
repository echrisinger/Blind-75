from typing import NamedTuple

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nodes: 'Mapping[int, boolean]' = {}
        for n in nums:
            if n not in nodes:
                nodes[n] = False
            
            if n-1 in nodes:
                nodes[n] = True
            
            if n+1 in nodes:
                nodes[n+1] = True
            
        sources = []
        for n, has_inbound in nodes.items():
            if not has_inbound:
                sources.append(n)
                
        max_run = 0
        for n in sources:
            curr_run = 1
            while (n + curr_run) in nodes:
                curr_run += 1
            
            max_run = max(curr_run, max_run)
        
        return max_run
