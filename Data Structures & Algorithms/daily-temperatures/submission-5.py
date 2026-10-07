class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # DP solution, compute and use the computed - no extra space

        # to work it, we know right-side of every index, solution will be there,
        # so start from right, copute and as you move left use that computed sol.

        n = len(temperatures)
        res = [0] * n
        
        for i in range(n-2, -1, -1):
            j = i + 1
            # in loop check untill it ends
            while j < n and temperatures[j] <= temperatures[i]:
                if not res[j]:
                    # make j to last index+1, so it break
                    j = n
                else:
                    # check on right, break if you reached end or grater value
                    # jump to this index and check if there is solution
                    j += res[j]

                    # in case if the result is 0(already computed), meaning no
                    # solution, because right side is already checked and
                    # computed
                    # and in main loop already checking if j<i, meas if no
                    # solution to grater value itslef, for sure smaller value
                    # will
                    # not have solution

            # as soon as loop breaks, i will have solution or reached end.
            if j < n:
                res[i] = j - i

        return res
        