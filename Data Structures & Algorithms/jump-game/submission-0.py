class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums) - 1

        for l in range(len(nums) - 2, -1, -1):
            if r - l <= nums[l]:
                r = l
        return r == 0
            