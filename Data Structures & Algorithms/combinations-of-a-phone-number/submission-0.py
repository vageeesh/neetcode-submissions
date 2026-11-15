class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        res = []

        def dfs(i, tmp):
            if len(tmp) >= len(digits):
                res.append(''.join(tmp))
                return

            for each in lookup[digits[i]]:
                tmp.append(each)
                dfs(i+1, tmp)
                tmp.pop()


        if digits:
            dfs(0, [])

        return res
