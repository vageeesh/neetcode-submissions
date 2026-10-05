class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # i felt easy this as easy problem,
        # just append numbers and when you saw symbol, retireve last 2
        # compute and store: start: 10.44PM, end:

        st = []
        r = 0
        for each in tokens:
            if each not in ('+', '-', '*', '/'):
                st.append(int(each))
            else:
                # retrieve 2 elements
                f = st.pop()
                s = st.pop()

                # operation
                if each == '+':
                    r = s + f
                elif each == '-':
                    r = s - f
                elif each == '*':
                    r = s * f
                else:
                    r = int(s / f)
                
                st.append(r)
        if not r:
            r = st.pop()
        return r