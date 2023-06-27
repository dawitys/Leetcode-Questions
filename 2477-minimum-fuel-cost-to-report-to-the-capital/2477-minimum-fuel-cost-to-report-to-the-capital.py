class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        #find the ones with degree == 1
        for start, end in roads:
            graph[start].append(end)
            graph[end].append(start)
            
            degree[start] += 1
            degree[end] += 1
            
        ppl = defaultdict(lambda : 1)
        
        queue = deque([n for n in graph if degree[n] == 1 and n != 0])
        fuel = 0
        
        while(queue):
            curr = queue.popleft()
            fuel += ceil(ppl[curr]/seats)
            
            for ne in graph[curr]:
                degree[ne] -= 1
                ppl[ne] += ppl[curr]
                if ne != 0 and degree[ne] == 1:
                    queue.append(ne)
                    
                    
        return fuel
                    
                    
                    
                