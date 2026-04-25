class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        found = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == '1' and (r, c) not in found:
                    count += 1
                    q.append([r, c])
                    while len(q) > 0:
                        row, col = q.popleft()
                        found.add((row, col))
                        adj = [[row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]]
                        for pos in adj:
                            if (pos[0] >= 0 and pos[1] >= 0 and pos[0] < len(grid)
                            and pos[1] < len(grid[0]) and grid[pos[0]][pos[1]] == "1"
                            and (pos[0], pos[1]) not in found):
                                q.append([pos[0], pos[1]])
        return count
