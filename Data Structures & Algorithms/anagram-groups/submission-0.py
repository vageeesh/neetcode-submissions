class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for each in strs:
            key = "".join(sorted(each))
            if key in hashmap:
                hashmap[key].append(each)
            else:
                hashmap[key] = [each]
        
        return list(hashmap.values())
