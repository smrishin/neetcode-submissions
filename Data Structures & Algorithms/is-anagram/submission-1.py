from collections import defaultdict, Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        
        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] += 1
            count[t[i]] -= 1
        
        for key, val in count.items():
            if val != 0:
                return False
        return True
