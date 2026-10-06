class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # checked the video and understood problem
        # idea: keep adding to array and when you found an element which
        # is grater than top element keep removing till you found no elements
        # smaller than this, because for all previous this is ans, 
        # contine with this idea till end - simple

        st = []
        # output order matters, so keep list with defaulut 0, and when we pop, use index and update that index element because even output order should be same as input order
        output = [0] * len(temperatures)

        for i, num in enumerate(temperatures):
            # if top is less than current num, then current num is ans,
            # so remove those
            # st contains both number and index, checking num here
            while st and st[-1][0] < num:
                poped = st.pop()
                # adding 1 to index as index start from 0
                output[poped[1]] = ((i - poped[1]))
            
            # append both number and index because we need to return the index,
            # so keep track of both
            st.append([num, i])
        
        # stack will have some elements for which no future day temp, but no need
        # to pop those and append 0, because we initialised with 0 at top
        return output





        