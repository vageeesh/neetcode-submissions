# This si not optimal solution
""" 2 problems:
    1. I am calculating frquency again and again
    2. incrementing i += 1 when window is not valid, this we should avoid and use while to increment until valid window
"""
class Solution:
    def get_frequent_ele(self, d):
        fr_v = 0
        for key, val in d.items():
            if val > fr_v:
               fr_v = val
               fr_w = key

        return fr_v, fr_w

    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        h = 0
        i, j = 0, 0

        while j < len(s):
            w = s[j]

            freq[w] += 1
            fr_v, fr_w = self.get_frequent_ele(freq)

            if (((j-i)+1) - fr_v) <= k:
                # we are with in the limit of valid window
                h = max(h, (j-i) + 1)
            else:
                freq[s[i]] -= 1
                i += 1
                
            # why j+=1 in both the cases ? Its because if you increment only i you can find another solution of same window length, which will not help, if you need better solution for sure window > current already known, so increase j as well
            # Also if i do only inside if: then my freq dict will become corrupt, because in a window i always adds jth index and compute freq, but here j will remain in same index and freq will be double calculated which will give wrong output
            j += 1

        return h
            
        