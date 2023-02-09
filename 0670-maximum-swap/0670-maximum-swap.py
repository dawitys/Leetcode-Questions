class Solution:
    def maximumSwap(self, num: int) -> int:
        ans  = num
        ns = list(str(num))
        for i in range(len(ns)):
            for j in range(len(ns)):
                ns[i],ns[j] = ns[j],ns[i]
                ans = max(ans,int(''.join(ns)))
                ns[i],ns[j] = ns[j],ns[i]
        
        return ans