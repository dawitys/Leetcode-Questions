class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        elements = path.split('/')
        
        for i in range(len(elements)):
            if elements[i] == '' or elements[i] == '.':
                continue
            if elements[i] == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(elements[i])
                
        return '/'+ '/'.join(stack)
        
            