class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        def dfs(node, arr, counter=0):
            while arr[node]==-1 and node!=-1:
                arr[node] = counter
                dfs(edges[node], arr, counter+1)
            return arr
        
        distance1 = [-1 for i in range(len(edges))]
        dfs(node1, distance1)
		
        distance2 = [-1 for i in range(len(edges))]
        dfs(node2, distance2)       
            
        res = float("inf")
        answer = -1
        
        for i in range(len(edges)):
            if distance1[i]!=-1 and distance2[i]!=-1:
                maximum_distance = max(distance1[i], distance2[i])		
                if maximum_distance < res:
                    res = maximum_distance
                    answer = i
                
        return answer
