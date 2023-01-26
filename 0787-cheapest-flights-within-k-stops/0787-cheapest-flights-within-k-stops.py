class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, destination, price in flights:
            graph[start].append((destination,price))
            
        pq = [(0,0,src)]
        
        cheapest = [[inf]*(k+1) for _ in range(n)]
        cheapest[src] = [0]*(k+1)
        
        while pq:
            current_price,stops,node = heappop(pq)
            
            for neighbour,price in graph[node]:

                if stops<=k and cheapest[neighbour][stops] > price + current_price:
                    cheapest[neighbour][stops] = price + current_price
                    heappush(pq,(cheapest[neighbour][stops],stops+1, neighbour))

        
        return min(cheapest[dst]) if min(cheapest[dst]) != inf else -1