class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        vcol = set()
        vpdia = set() # positive diagonal is r+c
        vndia = set() # negetive diagonal is r-c

        res = []
        tmp_board = [["."] * n for j in range(n)]

        def dfs(row, tmp_board):
            if row == n:
                c = []
                for each_row in tmp_board:
                    c.append("".join(each_row))
                
                res.append(c)
                return

            
            for col in range(n):
                if (col in vcol) or (row+col) in vpdia or (row-col) in vndia:
                    continue

                # place queen in this column
                tmp_board[row][col] = 'Q'

                # mark as visited
                vcol.add(col)
                vpdia.add(row+col)
                vndia.add(row-col)

                # recursive call
                dfs(row+1, tmp_board)

                # revert chocide
                vcol.remove(col)
                vpdia.remove(row+col)
                vndia.remove(row-col)
                tmp_board[row][col] = '.'

        dfs(0, tmp_board)
        return res

        