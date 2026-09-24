class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        parts = []

        for each in strs:
            if each == "":
                parts.append("-99")
            else:
                parts.append(each)

        return "-98".join(parts)


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

