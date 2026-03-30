class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        for l in range(len(s)):
            if not s[l].isalnum():
                continue
            while not s[r].isalnum():
                r -= 1
            left = s[l].lower()
            right = s[r].lower()
            if left != right:
                return False
            r-=1
        return True