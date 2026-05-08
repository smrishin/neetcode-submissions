class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # TD
        memo = {}

        def dp(remain):
            if remain in memo:
                return memo[remain]
            if remain <= 0:
                return 0
            
            res = float("inf")
            for coin in coins:
                if remain - coin >= 0:
                    res = min(res, 1 + dp(remain - coin))
            memo[remain] = res
            return res
        retVal = dp(amount)
        return retVal if retVal < float("inf") else -1
