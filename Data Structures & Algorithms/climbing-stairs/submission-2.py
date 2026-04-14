class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {
            1: 1,
            2: 2
        }

        def recSolve(n, memo):
            if n not in memo:
                memo[n] = recSolve(n - 1, memo) + recSolve(n - 2, memo)
            return memo[n]

        return recSolve(n, memo)