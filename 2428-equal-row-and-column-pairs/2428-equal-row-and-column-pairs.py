class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        row = {}
        result = 0

        for i in range(n):
            key = tuple(grid[i])
            row[key] = row.get(key, 0) + 1

        for j in range(n):
            key = tuple(grid[i][j] for i in range(n))
            result += row.get(key, 0)
        
        return result