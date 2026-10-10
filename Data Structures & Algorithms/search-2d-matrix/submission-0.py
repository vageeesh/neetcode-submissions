class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ta_lis = 0
        for each in matrix:
            if target > each[-1]:
                ta_lis += 1
        
        # now i know target list
        if ta_lis >= len(matrix):
            return False

        array = matrix[ta_lis]

        st, ed = 0, len(array)-1
        while st <= ed:
            mid = st + ((ed - st) // 2) 
            if array[mid] == target:
                return True
            elif array[mid] < target:
                st = mid + 1
            else:
                ed = mid - 1
        
        return False
