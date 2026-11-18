class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        dfs_dic = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in dic:
                return dic[i]
            else:
                if i+1 in dfs_dic:
                    dfs_1 = dfs_dic[i+1]
                else:
                    dfs_1 = dfs(i+1)

                if i+2 in dfs_dic:
                    dfs_2 = dfs_dic[i+2]
                else:
                    dfs_2 = dfs(i+2)

                dic[i] = cost[i] + min(dfs_1, dfs_2)
                return dic[i]


        return min(dfs(0), dfs(1))
             