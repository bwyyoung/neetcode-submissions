from collections import Counter


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsorted = sorted(nums)
        triplet = []
        triplet_counter = []
        t_i = 0
        length = len(numsorted)
        
        while t_i < length:
            left = t_i + 1
            right = length - 1
            while left < right:
                current_sum = numsorted[left] + numsorted[right]
                target = -numsorted[t_i]
                if current_sum == target:
                    t = [numsorted[left], numsorted[right], numsorted[t_i]]
                    if Counter(t) not in triplet_counter:
                        triplet_counter.append(Counter(t))
                        triplet.append(t)
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
            t_i += 1
        
        return triplet