class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2:
            return nums[0]

        n = len(nums)

        previous_2 = nums[0]
        previous_1 = max(previous_2, nums[1])

        for i in range(2, n):
            tmp = max(previous_1, previous_2 + nums[i])
            previous_2 = previous_1
            previous_1 = tmp

        return previous_1