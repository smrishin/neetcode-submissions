class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window optimized
        res = 0
        count = {}
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res

        # # sliding window
        # res= 0
        # charset = set(s)

        # for c in charset:
        #     count = l = 0
        #     for r in range(len(s)):
        #         if s[r] == c:
        #             count += 1
                
        #         while r-l+1 - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1
        #         res = max(res, r - l + 1)

        # return res