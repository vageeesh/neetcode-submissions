class Solution:
    def get_region(self, rn, cn):
        # only 3 parts so if we devide both rn,cl by 3 and check which part that should be good enough to indicate what region we are in
        rn //= 3 
        cn //= 3

        if cn == 0:
            if rn == 0:
                return "reg_1"
            elif rn == 1:
                return "reg_2"
            elif rn == 2:
                return "reg_3"
        elif cn ==1:
            if rn == 0:
                return "reg_4"
            elif rn == 1:
                return "reg_5"
            elif rn == 2:
                return "reg_6"
        elif cn ==2:
            if rn == 0:
                return "reg_7"
            elif rn == 1:
                return "reg_8"
            elif rn == 2:
                return "reg_9"

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import defaultdict
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        region_dict = defaultdict(list)

        total_len = len(board[0])

        for i in range(total_len):
            for j in range(total_len):
                val = board[i][j]

                if val == ".":
                    continue

                # check row
                if val in row_dict[i]:
                    return False
                
                # check column
                if val in col_dict[j]:
                    return False

                # check region
                rg_key = self.get_region(i, j)
                if val in region_dict[rg_key]:
                    return False

                # else update dict
                row_dict[i].append(val)
                col_dict[j].append(val)
                region_dict[rg_key].append(val)

        return True
        