class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 1:
            return True
                
        nodes = {
            i: set()
            for i in range(n)
        }
        
        for i1, i2 in edges:
            nodes[i1].add(i2)
            nodes[i2].add(i1)
            
        source = next((
            i
            for i in range(n)
            if len(nodes[i]) <= 1
        ), None)
        
        if source is None:
            return False
        
        stk = [source]
        while stk:
            node = stk.pop()
            if node not in nodes:
                return False
            children = nodes[node]        
            del nodes[node]
            
            explored_count = 0
            for i in children:
                if i not in nodes:
                    explored_count += 1
                else:
                    stk.append(i)
                    
            if explored_count > 1:
                return False
                        
        return len(nodes) == 0
