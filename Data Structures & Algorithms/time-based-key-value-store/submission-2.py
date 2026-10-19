class TimeMap:

    def __init__(self):
        self.r = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.r:
            self.r[key][timestamp] = value
            self.r[key]["all_timestamps"].append(timestamp)
        
        else:
            self.r[key] = {
                timestamp: value
            }
            self.r[key]["all_timestamps"] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.r:
            return ""
        
        d = self.r[key]
        t = timestamp
        while t >= 0:
            if t in d:
                return d[t]
            else:
                t -= 1

        return ""
