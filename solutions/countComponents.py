from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        
        tf = defaultdict(set)
        
        for edge in edges:
            t, f = edge
            
            tf[t].add(f)
            tf[f].add(t)
            
        print(tf)
            
        components = 0
        for i in range(n):
            if i in seen:
                continue
            
            subgraph_stack = [i]
            while subgraph_stack:
                curr = subgraph_stack.pop()
                if curr in seen:
                    continue
                
                seen.add(curr)
                for neighbor in tf[curr]:
                    subgraph_stack.append(neighbor)

            components += 1

        return components

