class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = nums[0]
        while l <= r:
            # check for 2 eleresnts:
            # when array devide and left with 2, then it may miss the other one
            # as mid may be bigger and only 2 eleresnts, so next iteration not happen
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            m = (l+r)//2
            # update min, if mid eleresnt is min
            res = min(res, nums[m])

            # if mid >, resaning elresnt will be on the left side
            if nums[m] >= nums[l]:
                l = m+1
            else:
                r = m-1

        return res
