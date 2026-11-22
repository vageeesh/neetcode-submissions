class Solution:
    def longestPalindrome(self, s: str) -> str:
        # solving using 2 pointer approach
        n = len(s)
        # we have to handle even and odd length in seperate
        max_l = 0
        max_s = ""
        
        # for odd length
        for i in range(n):
            p1, p2 = i, i
            while p1>=0 and p2<n and s[p1] == s[p2]:
                # record max length
                if (p2-p1)+1 > max_l:
                    max_l = (p2-p1)+1
                    max_s = s[p1:p2+1]
                
                p2 += 1
                p1 -= 1

        # for even length
        for i in range(n):
            p1, p2 = i, i+1

            while p1>=0 and p2<n and s[p1] == s[p2]:
                if (p2-p1)+1 > max_l:
                    max_l = (p2-p1)+1
                    max_s = s[p1:p2+1]
                
                p1 -= 1
                p2 += 1

        return max_s
