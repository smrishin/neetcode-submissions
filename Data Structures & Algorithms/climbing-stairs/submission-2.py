class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        dp = [0,1,2]
        
        for i in range(3, n+1):
            dp.append(dp[i-2] + dp[i-1])
        return dp[-1]