class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)- 1

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1