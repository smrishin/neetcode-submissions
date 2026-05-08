class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        res = 0

        def dfs(r, c):
            for ro, co in directions:
                nr, nc = r + ro, c + co

                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == '1':
                    grid[nr][nc] = '0'
                    dfs(nr, nc)

        
        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    dfs(r, c)
                    res += 1
        
        return res
