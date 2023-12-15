class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        seen = set()
        
        for s,d in paths:
            seen.add(s)
            
        for s,d in paths:
            if d not in seen:
                return d