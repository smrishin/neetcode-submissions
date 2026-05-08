class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TD
        memo = {0 : 0}

        def dp(remain):
            if remain in memo:
                return memo[remain]
            
            if remain < 0:
                return float("inf")
            
            coins_used = float("inf")
            for coin in coins:
                coins_used = min(coins_used, 1 + dp(remain - coin))
            
            memo[remain] = coins_used
            return coins_used
        
        res = dp(amount)

        return res if res < float("inf") else -1
