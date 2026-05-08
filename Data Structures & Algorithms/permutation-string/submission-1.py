class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        if s1 is longer than s2, then s1 cannot be part of s2 so return false

        now we need 3 things, 
        1. freq of each char in s1
        2. num of individual chars in s1
        3. total len of s1, 
        count the frequencies of each char in s1 -> this will have 1 and 2
        we can get 3 with len(s1)

        keep an empty counter to count s2's freq of individual chars to compare with s1 count
        keep a found counter (int) to count the individual chars that match our requiement, which is that char should be in s1.

        now start sliding window operations
        l will be 0, r will go from 0 to len(s2)

        for each r:
            add char at r to s2count

            if char at r is in s1 (or s1Count keys, same thing) and count of the char at r is equal in s1count and s2count then we found a char, so incrememnt found by 1
            now check if we met result criteria 
            while found == len(s1Count) which is num of unique chars in s1 are all found in s2:
                then if the current window is of s1 len means, we found all chars in s2 and these chars are in len (s1) which mean some permutation of s1 is this sub array so return true
                else:
                    make the window smaller by moving left pointer by 1
                    before moving left pointer we need to make sure s2count is decremented for that char at l and also if that char at l was to update found we need to lower found as well. 

        if the whole string is passed then we didnt find the permutation in s2 so return false 
        '''

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