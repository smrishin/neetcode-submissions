class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        dp = [[False] * n for _ in range(n)]

        for start in range(n - 1, -1, -1):
            for end in range(start, n):
                if s[start] == s[end] and (end - start <= 2 or dp[start + 1][end - 1]):
                    dp[start][end] = True
                    res += 1
        return res