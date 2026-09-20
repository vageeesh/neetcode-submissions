class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set()
        duplicate = False
        for each in nums:
            if each not in hashmap:
                hashmap.add(each)
            else:
                duplicate=True
                break
        return duplicate


        