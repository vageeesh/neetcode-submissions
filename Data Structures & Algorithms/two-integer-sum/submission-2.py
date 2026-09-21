class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solving using 2 pointer approach
        # since we sort the array, 2 pointer will work and will guide regarding when to increase/decrease the index and on which side

        # not modifiying original array and create new, also keeping track of original indexes
        new_arr = []
        for i, v in enumerate(nums):
            new_arr.append([i, v])
        
        # sort array based on the value | first element
        # if i append value first and then index then just sort() is enough because default behavior to sort is to sort using first element of nested array
        new_arr.sort(key=lambda x: x[1])

        i, j = 0, len(nums)-1
        while i<j:
            c_sum = new_arr[i][1] + new_arr[j][1]
            if c_sum == target:
                f_i, s_i = new_arr[i][0], new_arr[j][0]

                # if f_i < s_i:
                #     return [f_i, s_i]
                # else:
                #     return [s_i, f_i]
                
                return [min(f_i, s_i), max(f_i, s_i)]
            elif c_sum > target:
                # grater, so last element to be removed since sorted
                j -= 1
            else:
                # lesser, meaning need higher number, so increment
                i += 1
        
        # if nothing found
        return []





        
        