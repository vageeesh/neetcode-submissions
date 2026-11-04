class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # when question is like fid all possible - its backtrack sol

        res = []

        def dfs(tmp_array, index):
            if index >= len(nums):
                # append the result found so far to final res
                res.append(tmp_array.copy())
                # stop condition
                return

            tmp_array.append(nums[index])
            dfs(tmp_array, index + 1)
            # pop last element to check different combination
            tmp_array.pop()
            dfs(tmp_array, index + 1)

        dfs([], 0)
        return res