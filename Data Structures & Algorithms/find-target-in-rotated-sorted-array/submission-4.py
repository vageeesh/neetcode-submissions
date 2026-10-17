class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea: check which side of array(part) is sorted and try to put a bounding comparision on that side, which will help in letting know about what to eleminate
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            # check if left side sorted
            if nums[l] <= nums[m]:
                # now check if traget also on this side
                if target > nums[m] or target < nums[l]:
                    # now search on right
                    l = m + 1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    # check on left as this side it not
                    r = m-1
                else:
                    l = m+1


        return -1