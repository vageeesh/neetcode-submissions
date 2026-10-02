class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        b = 0
        e = len(numbers) - 1

        while True:
            c_sum = numbers[b] + numbers[e]
            if c_sum > target:
                # remove last number - since sorted, grater means i have to reduce it
                e -= 1
            elif c_sum < target:
                b += 1
            else:
                return [b+1,  e+1]

        