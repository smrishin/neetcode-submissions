class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count = Counter(s1)
        required = len(s1Count)

        s2Count = Counter()
        found = 0

        l = 0

        for r in range(len(s2)):
            s2Count[s2[r]] += 1
            if s2[r] in s1Count and s2Count[s2[r]] == s1Count[s2[r]]:
                found += 1

            while found == required:
                if r - l + 1 == len(s1):
                    return True
                s2Count[s2[l]] -= 1
                if s2[l] in s1Count and s2Count[s2[l]] < s1Count[s2[l]]:
                    found -= 1
                l += 1
        return False