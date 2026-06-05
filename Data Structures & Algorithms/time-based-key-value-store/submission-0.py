class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append((timestamp, value))
        elif key not in self.store:
            self.store[key]=[(timestamp,value)]


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        res=""
        left=0
        arr=self.store[key]
        right=len(arr)-1
        while left<=right:
            mid=(left+right)//2
            if arr[mid][0]<=timestamp:
                res=arr[mid][1]
                left=mid+1
            else:
                right=mid-1
        return res
        