class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hashmap = {}
        for each in s:
            if each in hashmap:
                l = hashmap[each]
                l[0] += 1
                hashmap[each] = l
            else:
                hashmap[each] = [1]
        
        for each in t:
            if each in hashmap:
                l = hashmap[each]
                if (len(l) < 2):
                    l.append(1)
                    hashmap[each] = l
                else:
                    l[1] += 1
                    hashmap[each] = l
            else:
                return False

        for key, val in hashmap.items():
            if len(val) < 2:
                return False
            elif val[0] != val[1]:
                return False
        
        return True

        
                
            
        