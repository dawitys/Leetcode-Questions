class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        ans = 0
        n,m = len(img1),len(img1[0])
        a_points = []
        b_points = []
        
        for i in range(n):
            for j in range(m):
                if img1[i][j] == 1:
                    a_points.append((i,j))
                if img2[i][j] == 1:
                    b_points.append((i,j))
                
        transformations = Counter()
        for ax,ay in a_points:
            for bx,by in b_points:
                transformations[(ax-bx,ay-by)] += 1
        
        return max(transformations.values()) if transformations else 0
                
        