class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        if source == target:
            return 0
        
        bus_stop = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                bus_stop[stop].append(i)
        
        visited = set()
        queue = deque([(source,1)])
        
        while queue:
            curr, buses = queue.popleft()
            for bus in bus_stop[curr]:
                if bus not in visited:
                    visited.add(bus)
                    for stop in routes[bus]:
                        if stop == target:
                            return buses
                        queue.append((stop, buses + 1))
                    
        return -1