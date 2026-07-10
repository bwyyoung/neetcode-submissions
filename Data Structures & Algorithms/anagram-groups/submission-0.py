from collections import Counter

class Solution:
    def is_anagram(self, s1:str, s2:str):
        s1_set = set(s1)
        if s1_set != set(s2):
            return False
        for s1_ch in s1_set:
            if s1.count(s1_ch) != s2.count(s1_ch):
                return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_anagram = []
        for st in strs:
            found = False
            for subg in group_anagram:
                if self.is_anagram(subg[0], st):
                    subg.append(st)
                    found = True
                    continue
            if not found:
                group_anagram.append([st])

        return group_anagram
