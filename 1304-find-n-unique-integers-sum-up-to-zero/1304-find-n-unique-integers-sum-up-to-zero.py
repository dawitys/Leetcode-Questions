class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = [0] * n
        
        for i in range(1,(n//2)+1):
            ans[i-1] = i
            ans[n-i] = -i
        
        return ans
            