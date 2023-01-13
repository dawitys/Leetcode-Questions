class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        
        longest = 0
        
        start,end = 0,0
        
        while(start <= end and end < len(s)):
            while(s[end] in seen):
                seen[s[start]] -= 1
                if seen[s[start]] == 0:
                    del seen[s[start]]
                start += 1
            seen[ s[end] ] = 1
            longest = max(longest,end - start + 1)
            
            end += 1
        
        return longest