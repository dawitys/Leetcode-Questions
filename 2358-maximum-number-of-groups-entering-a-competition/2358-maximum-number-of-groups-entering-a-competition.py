class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        jump = 1
        i = 0
        ans = 0
        while i + jump <= len(grades):
            i += jump
            jump += 1
            ans += 1
            
        return ans
            