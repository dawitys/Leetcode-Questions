class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        max_points = 1
        
        def reducefract(n, d):
            def gcd(n, d):
                while d != 0:
                    t = d
                    d = n%d
                    n = t
                return n
            greatest=gcd(n,d)
            n/=greatest
            d/=greatest
            return n, d
        
        for i,(x,y) in enumerate(points):
            slopes = defaultdict(int)
            for j in range(i+1,len(points)):
                px,py = points[j]
                mx,my = x-px, y-py
                slope = reducefract(mx,my)
                slopes[slope] += 1
            if slopes:
                max_points = max(max_points,max(slopes.values())+1)
        
        return max_points