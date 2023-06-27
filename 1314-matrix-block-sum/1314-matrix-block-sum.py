class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        dp = mat[::]
        
        for i in range(len(mat)):
            for j in range(1,len(mat[0])):
                dp[i][j] = dp[i][j-1] + mat[i][j]
        
        ans = [[0 for _ in range(len(mat[0]))] for _ in range (len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                for r in range(max(0,i-k),min(len(mat),i+k+1)):
                    ans[i][j] += dp[r][min(len(mat[0])-1,j+k)]
                    if j-k > 0:
                        ans[i][j] -= dp[r][j-k-1]
                        
        return ans