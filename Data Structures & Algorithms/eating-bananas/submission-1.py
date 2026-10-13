class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        left = 1
        right = max(piles)
        res = right
        while left <= right:
            # check what number works and keep updating result
            mid = (left + right) // 2
            cr = 0
            for each in piles:
                cr += math.ceil(each / mid)

            if cr > h:
                # then this solution is not possible, so i have to increase mid
                left = mid + 1
            else:
                # this solution works
                # update res
                res = min (mid, res)

                # check if any better solution available by decresing it
                right = mid - 1

        return res