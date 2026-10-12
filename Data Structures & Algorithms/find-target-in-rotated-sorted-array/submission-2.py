class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) -1

        while left <= right:
            m = (left + right) // 2
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[left]:
                if target >= nums[left] and target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            else:
                if target < nums[left] and target > nums[m]:
                    left = m + 1
                else:
                    right = m - 1

        return -1