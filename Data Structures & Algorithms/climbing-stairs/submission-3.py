class Solution:
    def climbStairs(self, n: int) -> int:
        
        # dp - store result and re-use
        dic = {}

        def rec(n):
            if n <= 2:
                if n > 0:
                    return n
                else:
                    return 0

            
            if n in dic:
                return dic[n]

            dic[n] = rec(n-1) + rec(n-2) 
            return dic[n]

        return rec(n)
