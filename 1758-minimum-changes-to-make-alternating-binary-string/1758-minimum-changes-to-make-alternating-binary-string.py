class Solution:
    def minOperations(self, s: str) -> int:
        prev = '0'
        count = 0
        for i in range(len(s)):
            if s[i] == prev:
                count += 1
            prev = '0' if prev=='1' else '1'
        prev = '1'
        count2 = 0
        for i in range(len(s)):
            if s[i] == prev:
                count2 += 1
            prev = '0' if prev=='1' else '1'
            
        return min(count,count2)