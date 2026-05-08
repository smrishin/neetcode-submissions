class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        reslen = float("inf")

        if len(t) > len(s):
            return ""

        tc = Counter(t)
        required = len(tc)

        sc = Counter()
        found = 0

        l = 0

        for r in range(len(s)):
            sc[s[r]] += 1
            if s[r] in tc and sc[s[r]] == tc[s[r]]:
                found += 1
            
            while found == required:
                if r - l + 1 < reslen:
                    res = s[l:r+1]
                    reslen = r - l + 1

                sc[s[l]] -= 1
                if s[l] in tc and sc[s[l]] < tc[s[l]]:
                    found -= 1
                l += 1
        return res
