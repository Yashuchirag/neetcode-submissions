class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        count = 0
        ans = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                count = 0
            else:
                count += 1
            ans = max(ans, count)
        return ans