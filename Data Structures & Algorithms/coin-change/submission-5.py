class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if not coins:
            return -1
        
        # BU
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for remain in range(amount + 1):
                if remain - coin >= 0:
                    dp[remain] = min(dp[remain], dp[remain - coin] + 1)
        return dp[-1] if dp[-1] < float("inf") else -1

        
        # # TD
        # memo = {0 : 0}

        # def dp(remain):
        #     if remain in memo:
        #         return memo[remain]
            
        #     if remain < 0:
        #         return float("inf")
            
        #     coins_used = float("inf")
        #     for coin in coins:
        #         coins_used = min(coins_used, 1 + dp(remain - coin))
            
        #     memo[remain] = coins_used
        #     return coins_used
        
        # res = dp(amount)

        # return res if res < float("inf") else -1
