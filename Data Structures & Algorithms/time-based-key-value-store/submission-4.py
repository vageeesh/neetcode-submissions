class TimeMap:

    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value, timestamp]]
        else:
            self.d[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # idea use binary search to search
        res = ""
        res_array = self.d.get(key, [])
        if not res_array:
            return res
        
        l = 0
        r = len(res_array) - 1
        while l <= r:
            m = (l+r) // 2

            # we have to find nearest to the timestampt(less or equla both accepted)
            if res_array[m][1] <= timestamp:
                l = m + 1
                # record this(so far) nearest val for time
                res = res_array[m][0]

                # # one optimisation, this is not needed, as time will remain O(logN)
                # # but if exact mid then just return
                # if res_array[m][1] == timestamp:
                #     return res

            else:
                r = m -1

        return res
        
