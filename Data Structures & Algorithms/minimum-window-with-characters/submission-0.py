class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1
        missing = len(t)

        left = 0
        best_start, best_len = 0, float('inf')

        for right, c in enumerate(s):
            if need.get(c, 0) > 0:
                missing -= 1
            need[c] = need.get(c, 0) - 1

            while missing == 0:
                if right - left + 1 < best_len:
                    best_start, best_len = left, right - left + 1
                lc = s[left]
                need[lc] += 1
                if need[lc] > 0:
                    missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_start:best_start + best_len]