class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        answer = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]
        answer2 = [[0 for i in range(len(mat[0]))] for j in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                answer[i][j] = sum([mat[i][l]  for l in range(max(0,j-k),min(len(mat[0]),j+k+1))]) 
        
        for i in range(len(answer[0])):
            for j in range(len(answer)):
                answer2[j][i] = sum([answer[l][i]  for l in range(max(0,j-k),min(len(mat),j+k+1))])  
                
        return answer2