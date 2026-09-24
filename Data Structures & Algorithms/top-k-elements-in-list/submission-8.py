class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
           hashmap[i] = (hashmap.get(i, 0)) + 1

        # initialise an array with same leght as input because max possible array for frequency is completely distinct elements which is N
        
        # use list comprehensive only but not [[]]* N which will not work as that will create reference and modifying one will modify all
        new_arr = [[] for i in range(len(nums))]
        for key,freq in hashmap.items():
            # doing -1, because array position start from 0, so lets say all elements are same then that will create out-of-rangge
            # another option is create array with len(nums) + 1
            new_arr[freq-1].append(key)
        
        return_array = []
        for i in range(len(new_arr)-1,-1,-1):
            for each in new_arr[i]:
                if len(return_array) < k:
                    return_array.append(each)
                else:
                    return return_array

        return return_array
