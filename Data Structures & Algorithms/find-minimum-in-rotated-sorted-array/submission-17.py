class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while right >=0:
            if left > 0 and nums[left] < nums[left - 1]:
                return nums[left]
            if right < len(nums) - 1 and nums[right] > nums[right + 1]:
                return nums[right + 1]
            left += 1
            right -= 1
        return nums[0]