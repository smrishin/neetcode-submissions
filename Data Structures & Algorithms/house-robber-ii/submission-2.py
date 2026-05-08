class Solution:
    def rob1(self, nums):
        memo = {}

        def dp(i):
            if i < 0:
                return 0
            
            if i not in memo:
                memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]
        
        return dp(len(nums) - 1)

    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        return max(self.rob1(nums[:-1]), self.rob1(nums[1:]))