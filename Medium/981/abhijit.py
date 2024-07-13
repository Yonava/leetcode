class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val =  self.map.get(key,-1)
        if val == -1:
            self.map[key] = [(value, timestamp)]
        else:
            self.map[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        l , r = 0 , len(values) - 1
        print("all_values", values)
        if timestamp < values[0][1]:
            return ""
        if timestamp > values[-1][1]:
            return values[-1][0]
        while r > l:
            if timestamp == 15:
                print("right pointer",values[r])
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] > timestamp:
                r = mid - 1
            else:
                l = mid - 1
        return values[r][0]
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set("test","val",1)
# param_2 = obj.get("test",1)
# print(param_2)