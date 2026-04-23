class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.addHelper(val)
        return self.nums[-self.k]

    def addHelper(self, val: int) -> int:
        self.nums.append(val)
        i = len(self.nums) - 1
        while i > 0 and self.nums[i] < self.nums[i - 1]:
            tmp = self.nums[i]
            self.nums[i] = self.nums[i - 1]
            self.nums[i - 1] = tmp
            i -= 1
        print(self.nums)
            