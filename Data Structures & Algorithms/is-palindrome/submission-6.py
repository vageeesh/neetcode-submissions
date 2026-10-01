class Solution:
    def check_alpha(self, w):
        w = ord(w)
        if (w >= 97 and w <=122) or (w >=65 and w <=90) or (w >= 48 and w <=57):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        # using 2 pointers
        l_p = 0
        r_p = len(s) - 1

        while l_p <= r_p:
            # first check if its a valid alphabet
            while (l_p < r_p) and not self.check_alpha(s[l_p]):
                l_p += 1
            while (r_p > l_p) and not self.check_alpha(s[r_p]):
                r_p -= 1

            # if valid make case insensitive
            lw = s[l_p].lower()
            rw = s[r_p].lower()

            if lw == rw:
                l_p += 1
                r_p -= 1
            else:
                return False

        return True

        