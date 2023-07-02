class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def check_valid(arr):
            for a in arr:
                if a != 0:
                    return False
            return True
        
        ans = 0
        
        def backtrack(idx,changes,processed):
            nonlocal ans
            if check_valid(changes):
                ans = max(ans,processed)
            if idx == len(requests)-1:
                return
            for i in range(idx+1,len(requests)):
                changes[requests[i][0]] -= 1
                changes[requests[i][1]] += 1
                backtrack(i,changes,processed+1)
                changes[requests[i][0]] += 1
                changes[requests[i][1]] -= 1
                
        transfers = [0]*n

        backtrack(-1,transfers,0)
        
        return ans