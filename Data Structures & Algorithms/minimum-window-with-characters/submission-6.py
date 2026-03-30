class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = Counter(t) 
        have = Counter()
        required_unique = len(need)
        formed = 0

        l = 0
        best_l, best_r = 0, len(s)

        for r, ch in enumerate(s):
            have[ch] += 1
            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required_unique:

                if r - l + 1 < best_r - best_l + 1:
                    best_l, best_r = l, r

                left_ch = s[l]
                have[left_ch] -= 1
                if left_ch in need and have[left_ch] < need[left_ch]:
                    formed -= 1
                l += 1

        if best_r == len(s):
            return ""
        return s[best_l:best_r+1]

