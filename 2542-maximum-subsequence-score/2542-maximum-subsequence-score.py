from heapq import heappush,heappop,heapify

class Solution:
    def maxScore(self, num1: List[int], num2: List[int], k: int) -> int:

        n = sorted(zip(num1,num2),key =lambda e:-e[1])
        running = sum(n[i][0] for i in range(k))
        min_heap = [n[i][0] for i in range(k)]
        heapify(min_heap)
        ans = n[k-1][1]*running
        for i in range(k,len(n)):
            running += n[i][0]
            heappush(min_heap,n[i][0])
            c = heappop(min_heap)
            running -= c
            ans = max(ans,n[i][1]*running)
        
        return ans
            