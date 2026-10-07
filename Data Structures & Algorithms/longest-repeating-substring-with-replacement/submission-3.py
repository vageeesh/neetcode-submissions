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
                j += 1
            else:
                freq[s[i]] -= 1
                i += 1
                j += 1

        return h
            
        