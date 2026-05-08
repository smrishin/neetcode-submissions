class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1c = Counter(s1)
        required = len(s1c)

        s2c = Counter()
        found = 0

        l = 0

        for r in range(len(s2)):
            rc = s2[r]

            s2c[rc] += 1

            if rc in s1c and s1c[rc] == s2c[rc]:
                found += 1

            while found == required:
                if r - l + 1 == len(s1):
                    return True
                
                lc = s2[l]
                s2c[lc] -= 1
                if lc in s1c and s2c[lc] < s1c[lc]:
                    found -= 1
                l += 1
        return False