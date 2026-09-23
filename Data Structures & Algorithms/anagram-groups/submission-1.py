from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimal solution, without sorting
        # O(n)
        hashmap = defaultdict(list)

        # since only lower case we know max size of array is 26
        for each in strs:
            c_lis = [0] * 26

            for i in each:
                c_lis[ord(i) - ord("a")] += 1

            hashmap[tuple(c_lis)].append(each)

        return list(hashmap.values())
        