class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numstore = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in numstore:
                return [numstore[complement], index]
            numstore[num] = index
