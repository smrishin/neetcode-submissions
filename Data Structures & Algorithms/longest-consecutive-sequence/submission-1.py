class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        res = 0

        for num in numSet:
            if num - 1 not in numSet:
                length = 1
                while num + 1 in numSet:
                    length += 1
                    num += 1
                res = max(length, res)
        return res