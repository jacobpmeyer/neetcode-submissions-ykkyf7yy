class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            p = target - num
            if p in d:
                return [d[p], i]
            else:   
                d[num] = i
        
        return [0, 0]