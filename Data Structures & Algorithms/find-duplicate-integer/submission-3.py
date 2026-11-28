class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # since each number is inclusive, once visited mark that as -ve

        for each in nums:
            if (nums[abs(each)-1]) < 0:
                return abs(each)
    
            nums[abs(each)-1] *= -1
        
        return -1