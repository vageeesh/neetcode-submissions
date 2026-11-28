class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # lets solve with O(n) first and then try to optimise
        dic = set()

        for i in nums:
            if i in dic:
                return i
            
            dic.add(i)

        return - 1

        