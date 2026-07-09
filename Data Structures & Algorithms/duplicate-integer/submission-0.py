class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for number in nums:
            if number in dict_nums:
                return True
            dict_nums[number] = number
        return False