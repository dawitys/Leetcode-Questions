class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count('1')
        length = len(s)
        res = ['1'] * (ones_count-1) 
        res += ['0'] * (length - ones_count) 
        res += ['1']
        
        return ''.join(res)
        