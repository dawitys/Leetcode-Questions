class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(numRows-1):
            row = []
            for j in range(len(ans[-1])-1):
                row.append(ans[-1][j]+ans[-1][j+1])
            ans.append([1] + row + [1])
            
        return ans