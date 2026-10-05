class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # keep set so the we can search and remove element in O(1) time
        st = 0
        end = 0
        un_set = set()
        max_len = 0

        while end < len(s):
            # check if char repeated
            end_ch = s[end]
            if end_ch not in un_set:
                # add
                un_set.add(end_ch)
            else:
                # already present, end_ch repeated
                # before proceeding calculate length
                max_len = max(max_len, (end-st))

                # now i have to remove from st till repeted char
                while s[st] != end_ch:
                    un_set.remove(s[st])
                    st += 1

                # if s[st] == end, this is the repeated char, remove this as well
                un_set.remove(s[st])

                # now add new char
                un_set.add(end_ch)
                st += 1
                    
            end += 1

        max_len = max(max_len, (end-st))

        return max_len
