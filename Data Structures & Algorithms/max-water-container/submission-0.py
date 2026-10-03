class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights) - 1

        max_storage = 0
        while s < e:
            width = (e-s)
            hi = min(heights[s], heights[e])

            c_s = width * hi
            if c_s > max_storage:
                max_storage = c_s
            
            # now i have to shift the pointer,
            # lets shift the low pointer to maximise getting another high one
            if heights[s] <= heights[e]:
                s += 1
            else:
                e -= 1
        return  max_storage

        