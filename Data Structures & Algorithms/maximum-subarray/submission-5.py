class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Divide n Conquer
        def dnc(l, r):
            if l > r:
                return float("-inf")
            
            curr = lmax = rmax = 0

            m = (l + r )//2

            for i in range( m - 1, l - 1, -1):
                curr += nums[i]
                lmax = max(curr, lmax)
            curr = 0
            for i in range(m + 1, r + 1):
                curr += nums[i]
                rmax = max(curr, rmax)

            currmax = lmax + rmax + nums[m]

            lhalf = dnc(l, m - 1)
            rhalf = dnc(m + 1, r)

            return max(lhalf, rhalf, currmax)
        return dnc(0, len(nums)-1)


        # # Kadane's algo
        # maxsum = nums[0]
        # curr = nums[0]

        # for num in nums[1:]:
        #     if curr < 0:
        #         curr = 0
        #     curr += num
        #     maxsum = max(maxsum, curr)

        # return maxsum