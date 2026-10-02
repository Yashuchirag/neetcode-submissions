class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set(nums)
        if len(nums) == 0:
            return False
        return len(nums) != len(temp)