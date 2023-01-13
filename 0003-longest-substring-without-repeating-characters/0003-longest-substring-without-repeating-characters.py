class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first_seen = {}
        
        longest = 0
        start = 0
        for i,c in enumerate(s):
            if c in first_seen and first_seen[c] >= start:
                start = first_seen[c] +1
            else:
                longest = max(longest,i-start+1 )
            first_seen[c] = i

            
        return longest