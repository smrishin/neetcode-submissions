class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kanade's Algo
        maxpro= nums[0]
        currmax = 1
        currmin = 1

        for num in nums:
            tmp = currmax * num
            currmax = max(currmax * num, currmin * num, num)
            currmin = min(tmp, currmin * num, num)
            maxpro = max(maxpro, currmax)
        
        return maxpro
