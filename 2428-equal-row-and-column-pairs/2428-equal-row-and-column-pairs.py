class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        result = 0
        row = {}
        col = {}

        for i in range(n):
            key = tuple(grid[i])
            row[key] = row.get(key, 0) + 1
        for j in range(n):
            ckey = tuple(grid[i][j] for i in range(n))
            col[ckey] = col.get(ckey, 0) + 1
        
        for key in row:
            if key in col:
                result += row[key] * col[key]
        
        return result