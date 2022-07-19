class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        
        for i in range(1,numRows):
            rows = [1]
            for j in range(1,i):
                rows.append(ans[-1][j]+ans[-1][j-1])
            rows = rows + [1]
            ans.append(rows)
            
        return ans
            
        