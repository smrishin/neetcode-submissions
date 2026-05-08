class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(remain):
            if remain == 0:
                return 0
            
            if remain in memo:
                return memo[remain]
            
            res = float("inf")

            for coin in coins:
                if remain - coin >= 0:
                    res = min(res, 1 + dfs(remain - coin))

            memo[remain] = res
            return res
        
        retVal = dfs(amount)

        return retVal if retVal < float("inf") else -1