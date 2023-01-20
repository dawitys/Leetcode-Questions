class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        M,N = len(grid[0]), len(grid)
        
        dp = [[ [grid[i][j] ,grid[i][j]] for i in range(N)] for j in range(M)]
        
        
        for i in range(1,M):
            dp[i][0][0] = dp[i][0][1] = dp[i][0][0] * dp[i-1][0][0]
        
        for j in range(1,N):
            dp[0][j][0] = dp[0][j][1] = dp[0][j][0] * dp[0][j-1][0]

        
        for i in range(1,M):
            for j in range(1,N):
                dp[i][j][0] = min( dp[i][j][0] * dp[i-1][j][0] , dp[i][j][0] * dp[i][j-1][0], dp[i][j][0] * dp[i-1][j][1] , dp[i][j][0] * dp[i][j-1][1])
                
                dp[i][j][1] = max( dp[i][j][1] * dp[i-1][j][0] , dp[i][j][1] * dp[i][j-1][0], dp[i][j][1] * dp[i-1][j][1] , dp[i][j][1] * dp[i][j-1][1])

        return dp[M-1][N-1][1] % (10**9 + 7) if dp[M-1][N-1][1] >= 0 else -1 