class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_sum = 1
        total_0 = 0
        re_lis = []

        for each in nums:
            if each == 0:
                total_0 += 1
            else:
                total_sum *= each
        
        if total_0 > 1:
            return [0] * len(nums)

        for each in nums:
            if total_0 == 1:
                if each == 0:
                    re_lis.append(total_sum)
                else:
                    re_lis.append(0)
            else:
                re_lis.append(total_sum//each)
        
        return re_lis


        