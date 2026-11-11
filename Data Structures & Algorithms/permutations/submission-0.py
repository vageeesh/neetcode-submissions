class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        per = self.permute(nums[1:])
        res = []
        for each in per:
            for i in range(0, len(each)+1):
                # you have to copy the whole array inside the second array
                # not outside, becuase, in each loop it will modify same, so create copy before doing any modifications
                each_copy = each.copy()
                each_copy.insert(i, nums[0])
                res.append(each_copy)

        return res

        
                
        