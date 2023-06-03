class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        employee_graph = defaultdict(list)
        
        for employee,managerid in enumerate(manager):
            if employee != headID:
                employee_graph[managerid].append(employee)
                
        def dfs(node):
            time = 0
            for subordinate in employee_graph[node]:
                time = max(dfs(subordinate),time)
            return time + informTime[node]
        
        return dfs(headID)