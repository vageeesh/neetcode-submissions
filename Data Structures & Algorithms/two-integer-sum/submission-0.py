class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        num_1 = num_2 = None
        for index, val in enumerate(nums):
            if target-val in hashmap:
                num_1 = hashmap[target-val]
                num_2 = index

            # if i not in hashmap:
            hashmap[val] = index

        if num_1 or num_2:
            if num_1 < num_2:
                return[num_1, num_2]
            else:
                return [num_2, num_1]
        else:
            return []

