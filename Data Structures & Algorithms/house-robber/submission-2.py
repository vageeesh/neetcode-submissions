class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dic = {}

        def dfs(i):
            if i >= len(nums):
                return 0

            if i in dic:
                return dic[i]
            
            c1 = nums[i] + dfs(i+2)
            c2 = dfs(i+1)

            dic[i] = max(c1, c2)

            return dic[i]

        return dfs(0)