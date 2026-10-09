class Solution:
    def bsearch(self, array, left, right, mid, target):
        if left > right:
            return -1
        
        mid = (left + right) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            return self.bsearch(array, mid + 1, right, mid, target)
        else:
            return self.bsearch(array, left, mid - 1, mid, target)

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        return self.bsearch(nums, left, right, 0, target)

        