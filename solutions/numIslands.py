class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not (grid and grid[0]):
            return 0
        
        sources = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    sources.append((row, col))
        
        count = 0
        for r,c in sources:
            if grid[r][c] == '-1':
                continue
            count += 1
            stk = [(r,c)]
            
            while stk:
                r, c = stk.pop()
                if grid[r][c] == '-1':
                    continue
                grid[r][c] = '-1'
                move_opts = [
                    (r-1, c),
                    (r+1, c),
                    (r, c-1),
                    (r, c+1),
                ]
                
                for nr, nc in move_opts:
                    if 0 <= nr < len(grid)\
                        and 0 <= nc < len(grid[0])\
                        and grid[nr][nc] == '1':
                        stk.append((nr,nc))
        
        return count

