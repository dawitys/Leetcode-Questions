class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        return all([arr[i]-arr[i-1]==arr[1]-arr[0] for i in range(2,len(arr))])