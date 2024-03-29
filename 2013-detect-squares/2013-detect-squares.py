class DetectSquares:

    def __init__(self):
        self.frequency = defaultdict(int)
        self.pair_points = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.frequency[x,y] += 1
        self.pair_points[x].add(y)
        

    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point
        for py in self.pair_points[x]:
            if py == y:
                continue
            dist = abs(py-y)
            ans += self.frequency[x,py] * self.frequency[x+dist,py] * self.frequency[x+dist,y] 
            ans += self.frequency[x,py] * self.frequency[x-dist,py] * self.frequency[x-dist,y] 

        return ans
    
# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)