class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        projects.sort()
        
        q = []
        ptr = 0
        for i in range(k):
            while ptr < len(profits) and projects[ptr][0] <= w:
                heappush(q, -projects[ptr][1])
                ptr += 1
            if not q:
                break

            w += -heappop(q)
            
        return w