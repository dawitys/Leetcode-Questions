class Solution:
    def checkValidString(self, s: str) -> bool:
        
        @cache
        def dfs(opens,i):
            if opens < 0:
                return False
            if i == len(s):
                return opens == 0
            if s[i] == '(':
                return dfs(opens+1,i+1)
            if s[i] == ')':
                return dfs(opens-1,i+1)
            if s[i] == '*':
                return dfs(opens+1,i+1) or dfs(opens-1,i+1) or dfs(opens,i+1)
            
        return dfs(0,0)