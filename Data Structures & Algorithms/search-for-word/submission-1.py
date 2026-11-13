class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        trows = len(board)
        tcolumns = len(board[0])
        # create m*n array and store visited as False
        vis = [[False for i in range(tcolumns)] for j in range(trows)]
        

        def dfs(ind, rcount, ccount):
            # if i equal to lenth meaning its not existed till now so all words are same
            if ind == len(word):
                return True

            if (rcount < 0) or (rcount >= trows) or (ccount < 0) or (ccount >=tcolumns) or word[ind] != board[rcount][ccount] or (vis[rcount][ccount]):
                return False

            
            vis[rcount][ccount] = True

            res = (dfs(ind+1, rcount+1, ccount) or dfs(ind+1, rcount, ccount+1) or dfs(ind+1, rcount-1, ccount) or dfs(ind+1, rcount, ccount-1))
            
            vis[rcount][ccount] = False

            return res


        dfs(0, 0, 0)

        for i in range(trows):
            for j in range(tcolumns):
                if dfs(0, i, j):
                    return True

        return False