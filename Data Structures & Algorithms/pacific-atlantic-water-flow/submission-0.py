class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac = set()
        atl = set()

        R = len(heights)
        C = len(heights[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(r, c, visited):
            for ro, co in directions:
                nr, nc = r + ro, c + co

                if (
                    0<=nr<R and 
                    0<=nc<C and 
                    heights[nr][nc] >= heights[r][c] and
                    (nr,nc) not in visited
                ):
                    visited.add((nr, nc))
                    dfs(nr, nc, visited)

        for c in range(C):
            pac.add((0, c))
            dfs(0, c, pac)

            atl.add((R-1, c))
            dfs(R-1, c, atl)
        
        for r in range(R):
            pac.add((r, 0))
            dfs(r, 0, pac)

            atl.add((r, C-1))
            dfs(r, C-1, atl)
        
        return list(pac.intersection(atl))

