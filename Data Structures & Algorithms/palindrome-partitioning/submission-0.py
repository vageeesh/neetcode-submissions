class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_valid_pal(i, j, s):
            while i<=j:
                if s[i] != s[j]:
                    return False

                i +=1
                j -= 1
            
            return True

        def dfs(start, tmparray):
            if start == len(s):
                # tmparray holds all valid combo, since reached end, save that
                res.append(tmparray.copy())

            for end in range(start, len(s)):
                if is_valid_pal(start, end, s):
                    tmparray.append(s[start: end+1])
                    dfs(end+1, tmparray)
                    tmparray.pop()

        dfs(0, [])

        return res