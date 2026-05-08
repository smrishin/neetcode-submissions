class Solution:
    def longestPalindrome(self, s: str) -> str:
        resI, resL = 0, 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True
        
        for i in range(n - 1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True

                    if resL < (j - i + 1):
                        resI = i
                        resL = j - i + 1
        
        return s[resI : resI + resL]



