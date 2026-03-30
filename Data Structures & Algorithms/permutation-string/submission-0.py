class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        PSEUDOCODE
        Let the length of s1 be l
        check all substrings of length l to see if they have the same letters
        when we move the window we subtract the letter on the left
        and add the one on the right
        '''
        from collections import Counter
        l = 0
        r = len(s1) - 1
        s1 = Counter(s1)
        while r < len(s2):
            window = Counter(s2[l:r + 1])
            if window == s1:
                return True
            r += 1
            l += 1

        return False