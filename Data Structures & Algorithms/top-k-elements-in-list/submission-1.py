class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countnum = {}
        numrank = [[] for i in range(len(nums) + 1)]
        mostfreq = []

        for num in nums:
            countnum[num] = 1 + countnum.get(num, 0)
        for number, count in countnum.items():
            numrank[count].append(number)
        for numrankgroup in reversed(numrank):
            for num in numrankgroup:
                mostfreq.append(num)
                if len(mostfreq) == k:
                    return mostfreq

        return mostfreq