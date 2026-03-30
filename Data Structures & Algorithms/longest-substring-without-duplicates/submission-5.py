class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lot = {}
        l = 0
        r = 0
        longest = 0
        for r in range(len(s)):
            # if we hit a repeat character
            if s[r] in lot.keys() and lot[s[r]] >= l:
                l = lot[s[r]] + 1
            lot[s[r]] = r
            longest = max(longest, r - l + 1)
        return longest

