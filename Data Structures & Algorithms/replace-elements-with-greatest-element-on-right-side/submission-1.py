class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)
        biggest = arr[-1]
        res[-1] = -1
        for i in range(len(arr) - 2, -1, -1):
            biggest = max(arr[i + 1], biggest)
            res[i] = biggest
        return res