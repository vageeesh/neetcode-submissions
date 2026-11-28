class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # since each number is inclusive, once visited mark that as -ve

        for each in nums:
            idx = abs(each)-1
            if (nums[idx]) < 0:
                return abs(each)
    
            nums[idx] *= -1
        
        return -1