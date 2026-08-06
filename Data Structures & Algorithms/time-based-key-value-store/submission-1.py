class TimeMap:

    def __init__(self):
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []

        self.keystore[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        left = 0
        cv = self.keystore.get(key, [])
        ans = ""
        right = len(cv)-1
        while left <= right:
            mid = (left+right)//2
            if cv[mid][1] <= timestamp:
                left = mid + 1
                ans = cv[mid][0]
            else:
                right = mid - 1
        return ans
        
            
        
