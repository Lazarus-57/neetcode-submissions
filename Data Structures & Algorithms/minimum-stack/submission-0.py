class MinStack:
    def __init__(self):
        self.stck=[]
        self.min_stck=[]

    def push(self, val: int) -> None:
        self.stck.append(val)
        if not self.min_stck:
            self.min_stck.append(val)
        else:
            self.min_stck.append(min(val,self.min_stck[-1]))
        return "null"

    def pop(self) -> None:
        self.stck.pop()
        return "null"

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return min(self.stck)