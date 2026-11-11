class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []

        # since there should not be duplicate, sort and move forward on repeat
        nums.sort()

        def dfs(i, ta):
            if i == len(nums):
                res.append(ta.copy())
                return

            ta.append(nums[i])
            dfs(i+1, ta)
            ta.pop()
            
            while (i < len(nums)-1) and nums[i] == nums[i+1]:
                i += 1

            dfs(i+1, ta)
        
        dfs(0, [])

        return res
