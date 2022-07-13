class Solution:
    def reverse(self, x: int) -> int:
        v = abs(x)
        reverse = int(str(v)[::-1]) 
        ans = reverse if x>0 else -reverse
        
        if ans >= 2**31 or ans < -(2**31):
            return 0
        return ans