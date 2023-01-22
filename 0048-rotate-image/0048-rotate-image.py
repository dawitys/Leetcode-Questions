class Solution:
    def rotate(self, box: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(box)
        
        for i in range(N//2 + N%2):
            for j in range(N//2):
                box[i][j], box[j][N-1-i], box[N-1-i][N-1-j], box[N-1-j][i] \
                    = box[N-1-j][i], box[i][j], box[j][N-1-i], box[N-1-i][N-1-j]
        

                