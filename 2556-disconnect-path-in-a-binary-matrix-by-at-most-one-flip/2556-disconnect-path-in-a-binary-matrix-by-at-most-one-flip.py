class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        diagonals = defaultdict(int)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    diagonals[j+i] += 1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == len(grid)-1 and j == len(grid[0]) -1:
                    continue
                if grid[i][j] == 1 and diagonals[j+i] <= 1:
                    return True
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    continue
                if i == len(grid)-1 and j == len(grid[0]) -1:
                    continue
                
                if diagonals[j+i] == 0:
                    return True
        
        return False
                