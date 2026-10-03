class Solution:
    def two_sum(self, nums, start, end, target):
        all_pairs = []
        while start < end:
            c_sum = nums[start] + nums[end]
            if c_sum == target:
                all_pairs.append([nums[start], nums[end]])
                # since we need not to stop here, and we have to find all the possible pairs, just increse the starting pointer and let it find all
                start += 1
                end -= 1

                # also if 2 numbers are same, then no need to repeat. check and skip
                while nums[start] == nums[start-1] and  start < end:
                    start += 1

            elif c_sum > target:
                end -= 1
            else:
                start += 1
        
        return all_pairs
        
        
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort it to avoid duplicate numbers in result
        sorted_array = sorted(nums)
        result_array = []
        t_len = len(sorted_array)
        for i in range(t_len-2):
            # avoiding the checks on same numbers
            if i !=0 and sorted_array[i-1] == sorted_array[i]:
                continue
            
            # i have to achieve 0 result, so target - current_number
            target = 0 - sorted_array[i]
            all_pairs = self.two_sum(sorted_array, i+1, t_len-1, target)
            if all_pairs:
                for each_pair in all_pairs:
                    result_array.append([sorted_array[i], each_pair[0], each_pair[1]])
        return result_array


        