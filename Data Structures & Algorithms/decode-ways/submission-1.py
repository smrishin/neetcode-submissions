class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # BU

        if s[0] == '0':
            return 0
        
        dp = [0] * n

        dp[0] = 1

        for i in range(1, n):
            res = 0

            if s[i] != "0":
                res += dp[i-1]
            
            if 10 <= int(s[i-1] + s[i]) <= 26:
                res += dp[i-2] if i-2 >= 0 else 1


            dp[i] = res
        return dp[-1]

        # # TD
        # memo = {}

        # def dp(i):
        #     if i in memo:
        #         return memo[i]
            
        #     if i == n:
        #         return 1
            
        #     if s[i] == '0':
        #         return 0
        #     res = dp(i+1)
        #     if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
        #         res += dp(i+2)
            
        #     return res
        
        # return dp(0)
