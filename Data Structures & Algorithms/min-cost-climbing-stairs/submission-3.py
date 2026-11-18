class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic = {}
        dfs_dic = {}

        def dfs(i):
            if i >= len(cost):
                return 0

            if i in dic:
                return dic[i]
            
            dic[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return dic[i]


        return min(dfs(0), dfs(1))
             