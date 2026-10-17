class Solution:
    def findMin(self, nums: List[int]) -> int:
        # if 1st elemetn less then last - direct ans break
        # compare first with mid:
            # if mid >=, then search right
            # if mid <, then search left 
            # if mid >=, but still min on left only possible if its completely sorted so check first and last element first < last - break loop, direct result

            # even it looks like rotated menas min can be on any side, mathmetically its not possible and it works on above logic
            
            # 1,2,3,4,5
            # 4,5,1,2,3
            # 3,4,5,1,2
            # 2,3,4,5,1


            l = 0
            r = len(nums) - 1
            res=nums[0]

            while l <= r:
                m = (l+r) // 2
                res = min(res, nums[m])

                if nums[l] < nums[r]:
                    res = min(res, nums[l])
                    break

                if nums[m] >= nums[l]:
                    l = m + 1
                else:
                    r = m - 1

            return res