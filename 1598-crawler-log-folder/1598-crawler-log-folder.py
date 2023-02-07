class Solution:
    def minOperations(self, logs: List[str]) -> int:
        steps = 0
        
        for log in logs:
            if log == './':
                continue
            if log == '../':
                if steps > 0:
                    steps -= 1
            else:
                steps += 1
                
        return steps