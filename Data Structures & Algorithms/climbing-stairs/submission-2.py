class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp - store result and re-use
        dic = {}

        def rec(n):
            if n <= 2:
                if n == 1:
                    return 1
                elif n == 2:
                    return 2
                else:
                    return 0

            
            if n in dic:
                return dic[n]

            dic[n] = rec(n-1) + rec(n-2) 
            return rec(n-1) + rec(n-2)

        return rec(n)
