class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        
        def dp(i):
            if i < 0:
                return 0

            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        
        return max(dp(n-1), dp(n-2))