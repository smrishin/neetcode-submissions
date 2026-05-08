class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <=2:
            return max(nums)
        # BU
        dp = [0] * (len(nums))

        dp[0], dp[1] = nums[0], max(nums[0],nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]


        # # TD
        # memo = {}
        # n = len(nums)
        
        # def dp(i):
        #     if i < 0:
        #         return 0

        #     if i not in memo:
        #         memo[i] = max(dp(i-1), dp(i-2) + nums[i])
        #     return memo[i]
        
        # return dp(n-1)