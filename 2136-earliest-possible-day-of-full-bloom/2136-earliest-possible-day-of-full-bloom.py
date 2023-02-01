class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = cur = 0
        for p,g in sorted(zip(plantTime,growTime),key=lambda x:-x[1]):
            cur+=p
            ans = max(ans,cur+g)
        return ans