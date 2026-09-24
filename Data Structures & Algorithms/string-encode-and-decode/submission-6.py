class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        ret_str = ""
        for i in range(len(strs)):
            each = strs[i]
            if each == "":
                to_append = "-99"
            else:
                to_append = f"{each}"
            
            if i == len(strs)-1:
                ret_str += to_append
            else:
                ret_str += f"{to_append}-98"

        
        return ret_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        
        new_l = s.split("-98")
        ret_lis = []
        for i in range(len(new_l)):
            if new_l[i] == "-99":
                ret_lis.append("")
            else:
                ret_lis.append(new_l[i])
        
        return ret_lis

