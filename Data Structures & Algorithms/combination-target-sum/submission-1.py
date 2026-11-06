class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # optimal way is to sort it
        nums.sort()
        res_a = []
        
        def dfs(index, tmp_a, t_sum):

            if index >= len(nums) or (t_sum >= target):

                if t_sum == target:
                    res_a.append(tmp_a.copy())

                return
                
            tmp_a.append(nums[index])
            dfs(index, tmp_a, t_sum + nums[index])
            # pop element
            tmp_a.pop()
            dfs(index + 1, tmp_a, t_sum)


        dfs(0, [], 0)
        return res_a

            

