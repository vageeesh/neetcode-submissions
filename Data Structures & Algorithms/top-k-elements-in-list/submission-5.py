class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        # initialise an array with same leght as input because max possible array for frequency is completely distinct elements which is N
        # new_arr=[[]]*(len(nums)+1)
        new_arr = [[] for i in range(len(nums) + 1)]
        for key,freq in hashmap.items():
            new_arr[freq].append(key)
        
        return_array = []
        for i in range(len(new_arr)-1,-1,-1):
            for each in new_arr[i]:
                if len(return_array) < k:
                    return_array.append(each)
                else:
                    return return_array

        return return_array
