class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ones_in_row = defaultdict(int)
        ones_in_col = defaultdict(int)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    ones_in_row[i] += 1
                    ones_in_col[j] += 1
                    
        count = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and ones_in_col[j] == 1 and ones_in_row[i] == 1:
                    count += 1
        
        return count