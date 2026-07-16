class Solution:
    def recursive_search(self, nums: List[int], target: int, left:int, right:int) -> int:
        if right - left == 0:
            if target == nums[left]:
                return left
            return -1
        midpoint = left + (right - left) // 2
        ## first_half = nums[:midpoint]
        ## second_half = nums[midpoint:]
        print(f"midpoint  {midpoint}" )
        if target <= nums[midpoint] and target >= nums[left]:
            print(f"first half {left} {midpoint}")
            return self.recursive_search(nums, target, left, midpoint)
        if nums[left] > nums[midpoint]:
            if target <= nums[midpoint] or target >= nums[left]:
                print(f"first half {left} {midpoint}")
                return self.recursive_search(nums, target, left, midpoint)
        print(f"second half {midpoint + 1} {right}")
        return self.recursive_search(nums, target, midpoint + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        return self.recursive_search(nums, target, left, right)
        
