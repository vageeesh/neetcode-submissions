class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # idea: check which side of array(part) is sorted and try to put a bounding comparision on that side, which will help in letting know about what to eleminate

        # this is also same solution as other, only change is once i know if the target on left/right part, i will make sure that element on that side using bounding the AND condition. it will make sure if target between a portion using AND and search in that

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            
            # check if left side sorted
            if nums[l] <= nums[m]:
                if target <= nums[m] and target >= nums[l]:
                    r = m-1
                else:
                    l = m + 1
            else:
                if target >= nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1


        return -1