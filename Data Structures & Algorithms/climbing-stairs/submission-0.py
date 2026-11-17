class Solution:
    def climbStairs(self, n: int) -> int:

        # dp - using the previous solution
        if n<=2:
            return n

        first_step = 1
        sec_step = 2
        cur = 0

        for i in range(3, n+1):
            cur = first_step + sec_step
            first_step = sec_step
            sec_step = cur

        return cur


        

        