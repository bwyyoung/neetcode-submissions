class Solution:
    def recursive_search(self, curlength:int, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target == nums[0]:
                return curlength
            return -1
        midpoint = len(nums) // 2
        first_half = nums[:midpoint]
        second_half = nums[midpoint:]
        if target <= first_half[-1] and target >= first_half[0]:
            print(f"first half {first_half}")
            return self.recursive_search(curlength, first_half, target)
        if first_half[0] > first_half[-1]:
            if target <= first_half[-1] or target >= first_half[0]:
                print(f"first half {first_half}")
                return self.recursive_search(curlength, first_half, target)
        curlength += len(first_half)
        print(f"second half {second_half}")
        return self.recursive_search(curlength, second_half, target)

    def search(self, nums: List[int], target: int) -> int:
       return self.recursive_search(0, nums, target)
        
