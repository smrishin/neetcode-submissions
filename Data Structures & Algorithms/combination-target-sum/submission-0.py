class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def bt(i, curr, total):
            if i >= len(nums):
                return
            if total > target:
                return
            
            if total == target:
                res.append(curr[:])
                return
            
            bt(i + 1, curr, total)
            curr.append(nums[i])
            total += nums[i]
            bt(i, curr, total)
            curr.pop()
            total -= nums[i]


        bt(0, [], 0)
        return res