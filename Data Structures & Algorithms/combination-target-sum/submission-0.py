class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        t_sum = 0

        tmp_a = []
        res_a = []

        def dfs(index):
            nonlocal t_sum

            if index >= len(nums) or (t_sum >= target):

                if t_sum == target:
                    res_a.append(tmp_a.copy())

                return
                
            tmp_a.append(nums[index])
            
            t_sum += nums[index]
            dfs(index)
            
            # pop element
            p = tmp_a.pop()
            # substract that poped
            t_sum -= p

            dfs(index + 1)

            # # pop element
            # p = tmp_a.pop()
            # # substract that poped
            # t_sum -= p

            # dfs(index + 1)

        dfs(0)
        return res_a

            

