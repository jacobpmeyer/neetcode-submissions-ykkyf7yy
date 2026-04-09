class MinStack:

    def __init__(self):
        self.minn = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.minn) == 0:
            self.minn.append(val)
        else:
            self.minn.append(min(val, self.minn[-1]))

    def pop(self) -> None:
        self.arr.pop()
        self.minn.pop()
        return None

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.minn[-1]
