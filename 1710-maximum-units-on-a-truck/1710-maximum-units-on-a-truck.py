class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda a:-a[1])
        
        ans = boxes = i = 0
        while(boxes < truckSize and i<len(boxTypes)):
            box = min(truckSize - boxes, boxTypes[i][0])
            ans += box * boxTypes[i][1]
            boxes += box
            i += 1
            
        return ans
            
        