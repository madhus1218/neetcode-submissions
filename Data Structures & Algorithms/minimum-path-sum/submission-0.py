class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 

        T = [[0] * n for _ in range(m)]
        T[0][0] = grid[0][0]

        for i in range(1, m):
            T[i][0] = T[i-1][0] + grid[i][0]

        for j in range(1, n):
            T[0][j] = T[0][j-1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = min(T[i][j-1], T[i-1][j]) + grid[i][j]
        
        return T[m - 1][n - 1]


        