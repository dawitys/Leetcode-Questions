class Solution:
    def isPalindrome(self,start, end, s):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        
        while(start <= end):
            if s[start] != s[end]:
                return self.isPalindrome(start+1,end,s) or self.isPalindrome(start,end-1,s)
            start += 1
            end -= 1
            
        return True