class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        R = len(board)
        C = len(board[0])

        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        self.visited = set()
        self.found = False
        def bt(r, c, i):
            if i == len(word):
                self.found = True
                return

            self.visited.add((r,c))

            for ro, co in directions:
                nr, nc = r + ro, c + co
                if 0<=nr<R and 0<=nc<C and board[nr][nc] == word[i] and (nr, nc) not in self.visited:
                    bt(nr, nc, i + 1)
                if self.found:
                    return

            self.visited.remove((r,c))

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0]:
                    bt(r, c, 1)
                    if self.found:
                        return True
        
        return False

        
