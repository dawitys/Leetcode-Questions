class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        
        for i in range(k):
            if s[i] in 'aeiou':
                l += 1
        ans = l
        for i in range(k,len(s)):
            if s[i] in 'aeiou':
                l += 1
            if s[i-k] in 'aeiou':
                l -= 1
            ans = max(ans,l)
        
        return ans