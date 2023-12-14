class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowOnes = defaultdict(int)
        colOnes = defaultdict(int)
        rowZeros = defaultdict(int)
        colZeros = defaultdict(int)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rowOnes[i] += 1
                    colOnes[j] += 1
                    
                if grid[i][j] == 0:
                    rowZeros[i] += 1
                    colZeros[j] += 1
                    
        ans = [[0]*len(grid[0]) for _ in range(len(grid))]
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                
                ans[i][j] +=  rowOnes[i] + colOnes[j] - rowZeros[i] - colZeros[j]
                
        return ans