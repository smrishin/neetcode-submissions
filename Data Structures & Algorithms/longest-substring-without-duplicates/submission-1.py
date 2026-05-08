class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        prevloc = {}
        res = 0
        l = 0

        for r in range(len(s)):
            if s[r] in prevloc:
                l = max(prevloc[s[r]] + 1, l)
            prevloc[s[r]] = r
            res = max(res, r - l + 1)

        return res