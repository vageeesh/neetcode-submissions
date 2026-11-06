class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sort, ooptimal
        candidates.sort()
        res = []

        def dfs(index, ta, ts):
            if ts == target:
                res.append(ta.copy())
                return

            if (index >= len(candidates)) or ts > target:
                return
            
            ta.append(candidates[index])
            dfs(index+1, ta, ts + candidates[index])
            

            while (index+1) < len(candidates) and (candidates[index] == candidates[index +1]):
                index += 1

            ta.pop()
            dfs(index+1, ta, ts)
        
        dfs(0, [], 0)
        return res


            
