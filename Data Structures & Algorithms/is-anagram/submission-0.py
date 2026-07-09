class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = {}
        for char in s:
            if char not in counter:
                counter[char] = 0
            counter[char] += 1
        for char in t:
            if char not in counter:
                return False
            counter[char] -= 1
        for val in counter.values():
            if val != 0:
                return False
        return True