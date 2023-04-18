class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        point, distance = -1, float('inf')        
        for i,(px, py) in enumerate(points):
            if (px == x or py == y) and abs(x-px)+abs(y-py) < distance:
                point = i
                distance = abs(x-px)+abs(y-py) 
        
        return point