class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # optimal approach using dict instead of set
        # idea is to use dict with value as index
        dic = {}
        st = 0
        max_length = 0
        # since storing index in dict, dont need start pointer
        for end in range(0, len(s)):
            if s[end] in dic:
                # reason for using max: since we are not deleting any key from dict,
                """its not only enough to consider the index of found key but also we
                should consider index only if that letter exists after start pointer,
                because if not that letter may exists because of earlier and may use that
                which is wrong.
                ex: abcdefhijklmnha: here i found h and a, but ideally after first h i
                should have delete all till h, meaning a also if not, next a it will
                consider as already there i dict, to avoid if you check st pointer then
                works as before st ignore, so max will help to consider from st or grater
                """
                # adding +1 to start becase next start should on next letter of last
                # found letter's index
                st = (max(st, dic[s[end]] + 1)) 
            
            # update dict with letter as key and index as val
            dic[s[end]] = end
            

            # update the max length
            max_length = max(max_length, (end-st)+1)

        return max_length
    
        