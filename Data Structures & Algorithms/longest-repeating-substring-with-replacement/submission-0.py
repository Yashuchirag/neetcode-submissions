class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = max_freq = best = 0
        for right, c in enumerate(s):
            count[c] = count.get(c, 0) + 1
            max_freq = max(max_freq, count[c])
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best