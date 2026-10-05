class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}          
        best = left = 0
        for right, c in enumerate(s):
            if last.get(c, -1) >= left:
                left = last[c] + 1
            last[c] = right
            best = max(best, right - left + 1)
        return best

