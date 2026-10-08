class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter
        # I am thinking to solve using window of size s1, and keep frequency count and total to match s1's freq
        ws = min(len(s1), len(s2))
        i, j = 0, 1

        # compute the first window
        news = s2[i]
        while j < ws:
            news += s2[j]
            j += 1
        
        if Counter(news) == Counter(s1):
            return True


        while j < len(s2):
            # always increment i,j and slide the window till last or you found sol.
            # before sliding i, compute
            # remove first occurence
            news = news.replace(s2[i], "", 1)
            news += s2[j]

            if Counter(news) == Counter(s1):
                return True
            
            j += 1
            i += 1
        
        return False


        