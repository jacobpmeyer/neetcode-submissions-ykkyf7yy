class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        i = len(stones) - 2
        while i >= 0:
            x = stones[i]
            y = stones[i + 1]
            res = abs(x - y)
            stones[i + 1] = 0
            stones[i] = res
            if res == 0:
                i -= 1
            else:
                j = i
                while j >= 1 and stones[j] < stones[j - 1]:
                    tmp = stones[j]
                    stones[j] = stones[j - 1]
                    stones[j - 1] = tmp
                    j -= 1
            i -= 1
        return stones[0]