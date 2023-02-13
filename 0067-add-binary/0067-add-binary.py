class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        
        if len(a) > len(b):
            b = ('0'*(len(a)-len(b)) ) + b
            
        elif len(a) < len(b):
            a = ('0'*(len(b)-len(a)) ) + a

        carry = 0
        for i in range(len(b)-1,-1,-1):
            add = int(a[i]) + int(b[i]) + carry
            if add > 1:
                carry = 1
            else:
                carry = 0

            if add%2 == 1:
                ans.append('1')
            else:
                ans.append('0')
        
        if carry:
            ans.append('1')
        
        
        return ''.join(ans[::-1])