class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def check_max(tnums):
            dic = {}
            def dfs(i):
                if i >= len(tnums):
                    return 0

                if i in dic:
                    return dic[i]

                c1 = tnums[i] + dfs(i+2)
                c2 = dfs(i+1)

                dic[i] = max(c1, c2)
                return dic[i]

            return dfs(0)

        if len(nums) == 1:
            return nums[0]

        # return check_max(nums[1:n])
        v1 = check_max(nums[0:n-1])
        v2 = check_max(nums[1:n])
        return max(v1, v2)
