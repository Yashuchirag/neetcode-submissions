class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = [0] * 26
        for c in s1:
            need[ord(c) - ord('a')] += 1

        left = 0
        for right, c in enumerate(s2):
            i = ord(c) - ord('a')
            need[i] -= 1
            while need[i] < 0:
                need[ord(s2[left]) - ord('a')] += 1
                left += 1
            if right - left + 1 == len(s1):
                return True
        return False
