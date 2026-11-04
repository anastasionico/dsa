class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        values = self.store.get(key, [])
        
        l, r = 0, len(values) -1
        
        while l <= r:
            m = ( l + r) // 2    
            
            if timestamp < values[m][0]:
                r = m - 1
            else:
                res = values[m][1]
                l = m + 1
            
        return res

if __name__ == "__main__":
    obj = TimeMap()
    obj.set("foo","bar",1)
    param_2 = obj.get("foo",1)
    param_2 = obj.get("foo",3)
    obj.set("foo","bar2",4)
    param_2 = obj.get("foo",4)
    param_2 = obj.get("foo",5)