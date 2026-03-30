class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sFreqs = {}
        tFreqs = {}
        for i in range(len(s)):
            sChar = s[i]
            tChar = t[i]
            if sChar in sFreqs.keys():
                sFreqs[sChar] += 1
            else:
                sFreqs[sChar] = 1
            if tChar in tFreqs.keys():
                tFreqs[tChar] += 1
            else:
                tFreqs[tChar] = 1
        return tFreqs == sFreqs