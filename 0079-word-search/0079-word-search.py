class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(ind, i, j):
            if self.Found: return        #early stop if word is found

            if ind == k:
                self.Found = True                #for early stopping
                return 

            if i < 0 or i >= m or j < 0 or j >= n: return 
            tmp = board[i][j]
            if tmp != word[ind]: return

            board[i][j] = "#"
            for x, y in [[0,-1], [0,1], [1,0], [-1,0]]:
                dfs(ind + 1, i+x, j+y)
            board[i][j] = tmp
        
        self.Found = False
        m, n, k = len(board), len(board[0]), len(word)
        
        for i, j in product(range(m), range(n)):
            if self.Found: return True          #early stop if word is found
            dfs(0, i, j)
        return self.Found
        ''' 
        def dfs(i,j,idx):
            if (not 0<=i<len(board)) or (not 0<=j<len(board[0])):
                return False
            if board[i][j]== word[idx] and idx == len(word)-1:
                return True
            res = dfs(i+1,j,idx+1) or  dfs(i,j+1,idx+1) or  dfs(i-1,j,idx+1) or  dfs(i,j-1,idx+1)
            if board[i][j] == word[0]:
                return res or dfs(i,j,0)
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    return dfs(i,j,0)
            '''

                        