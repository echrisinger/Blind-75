MOVES = [
    (1,0),
    (0,1),
    (-1,0),
    (0,-1),
]
class Solution:
    def pacificAtlantic(self, m: List[List[int]]) -> List[List[int]]:
        if not m or not m[0]:
            return []
        
        pacific_stk = [
            (r, 0)
            for r in range(len(m))
        ] + [
            (0, c)
            for c in range(len(m[0]))
        ]
        pacific = self.dirAscDFS(m, pacific_stk)
        
        atlantic_stk = [
            (r, len(m[0])-1)
            for r in range(len(m))
        ] + [
            (len(m)-1, c)
            for c in range(len(m[0]))
        ]
        atlantic = self.dirAscDFS(m, atlantic_stk)
        
        return list(pacific.intersection(atlantic))

    def dirAscDFS(self, m, stk):
        res = set()
        while stk:
            r, c = stk.pop()
            if (r,c) in res:
                continue
            res.add((r,c))
            for r_d, c_d in MOVES:
                n_r = r+r_d
                n_c = c+c_d
                if 0 <= n_r < len(m)\
                    and 0 <= n_c < len(m[0])\
                    and m[r][c] <= m[n_r][n_c]:
                    stk.append((n_r, n_c))
            
        return res

# time: O(n), space: O(n) -- constant num edges per vertex    
