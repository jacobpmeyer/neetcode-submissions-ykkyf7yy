class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = [0 for i in operations]
        pos = 0
        for op in operations:
            if op == "+":
                res[pos] += res[pos - 1] + res[pos - 2]
            elif op == "D":
                res[pos] = res[pos - 1] * 2
            elif op == "C":
                pos -= 1
                res[pos] = 0
                pos -= 1
            else:
                res[pos] = int(op)
            pos += 1
        return sum(res)