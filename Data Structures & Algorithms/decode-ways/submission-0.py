class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        memo = {}

        def dp(i):
            if i in memo:
                return memo[i]
            
            if i == n:
                return 1
            
            if s[i] == '0':
                return 0
            res = dp(i+1)
            if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
                res += dp(i+2)
            
            return res
        
        return dp(0)
