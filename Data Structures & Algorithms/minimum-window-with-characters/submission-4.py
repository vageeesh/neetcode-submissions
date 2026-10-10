class Solution:
    def minWindow(self, s: str, t: str) -> str:
        td = {}
        for each in t:
            td[each] = td.get(each, 0) + 1

        # track only unique, later we can check if each equlas to what we have or not
        need = len(td.keys())
        have = 0
        lr = [-1, -1]
        # initialise with max val, as we have to find min
        min_l = float("infinity")
        l = 0
        sd = {}

        for r, val in enumerate(s):
            # add val to sd dict
            sd[val] = sd.get(val, 0) + 1

            # increment have if we have a valid char
            if val in td and sd[val] == td[val]:
                have += 1

            # check if our need and have are equal
            while have == need and l <= r:
                new_l = (r-l) + 1
                # check if minimum avilable and update pointers & length
                if new_l < min_l:
                    min_l = new_l
                    lr[0] = l
                    lr[1] = r

                # next task is to find any better min available
                # move s meaning, decrement it from dict
                sd[s[l]] = sd[s[l]] - 1
                # since we decremented, if it reomoved valid char,
                # then decrement have as well, else no
                if s[l] in td and sd[s[l]] < td[s[l]]:
                    have -= 1

                l += 1

        return s[lr[0]: lr[1]+1] if min_l != float("infinity") else ""



