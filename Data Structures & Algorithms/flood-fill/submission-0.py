class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque()
        q.append([sr,sc])
        ROWS = len(image)
        COLS = len(image[0])
        original = image[sr][sc]
        while len(q) > 0:
            r, c = q.popleft()
            image[r][c] = color
            adj = [[r + 1, c],[r - 1, c],[r, c + 1],[r, c - 1]]
            for pos in adj:
                row, col = pos
                if (row >= 0 and row < ROWS and
                col >= 0 and col < COLS and
                image[row][col] == original and image[row][col] != color):
                    q.append([row, col])
        return image