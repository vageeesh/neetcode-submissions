class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        st = []

        for i, v in enumerate(heights):
            if not st:
                st.append([i, v])
            
            pe = None
            while st and st[-1][1] > v:
                pe = st.pop()
                # pop all which are grater than current value
                max_area = max(max_area, ((i-pe[0]) * pe[1]))

            # append current element to st with updated index
            if pe:
                st.append([pe[0], v])
            else:
                st.append([i, v])
        
        v = len(heights)
        while st:
            pe = st.pop()
            max_area = max(max_area, ((v-pe[0]) * pe[1]))

        return max_area

        