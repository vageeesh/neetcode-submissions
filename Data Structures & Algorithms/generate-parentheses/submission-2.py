class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        tarray = []

        def dfs(l_count, r_count):
            
            if l_count == r_count == n:
                res.append(''.join(tarray.copy()))
                return

            if l_count < n:
                tarray.append('(')
                dfs(l_count +1, r_count)
                tarray.pop()

            
            if r_count < l_count:
                tarray.append(')')
                dfs(l_count, r_count+1)
                tarray.pop()

        dfs(0, 0)
        return res
            
