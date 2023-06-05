class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        coordinates.sort(key=lambda a:a[1])
        
        def slope(p1,p2):

            return (p2[1]-p1[1]) / (p2[0] - p1[0]) if ( p2[0] - p1[0] != 0) else float('inf')
        
        p1,p2 = coordinates[:2]

        intial_slope = slope(p1,p2)
        print(intial_slope)
        
        for i in range(2,len(coordinates)):
            point = coordinates[i]
            print(slope(p1,point))
            if slope(p1,point) != intial_slope:
                return False
        
        return True