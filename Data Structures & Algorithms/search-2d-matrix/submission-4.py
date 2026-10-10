class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ta_lis = 0
        st, ed = 0, len(matrix)-1
        while st <= ed:
            mid = (st+ed) // 2
            if  matrix[mid][0] <= target and  matrix[mid][-1] >= target:
                ta_lis = mid
                break
            elif target > matrix[mid][-1]:
                st += 1
            else:
                ed -= 1
        
        # now i know target list
        if ta_lis >= len(matrix):
            return False

        array = matrix[ta_lis]

        st, ed = 0, len(array)-1
        while st <= ed:
            mid = (ed + st) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                st = mid + 1
            else:
                ed = mid - 1

        return False
