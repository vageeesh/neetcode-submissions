class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # idea - start from last and see at each position what is min and update with it

        for i in range(len(cost)-3, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])

        return min(cost[0], cost[1])