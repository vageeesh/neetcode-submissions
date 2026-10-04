class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for each in s:
            if each in ["(", "{", "["]:
                st.append(each)
            else:
                # if no elements to pop, then some imbalence so return False
                if not st:
                    return False

                p_e = st.pop()
                if not ((each == ")" and p_e == "(") or (each == "]" and p_e == "[") or (each == "}" and p_e == "{")):
                    return False

        return True if not st else False

        
        