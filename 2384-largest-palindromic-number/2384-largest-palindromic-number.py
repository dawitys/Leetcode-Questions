class Solution:
    def largestPalindromic(self, num: str) -> str:

        counter = Counter(num)
        res = []
        for c in '9876543210':
            if counter[c]>1 and (res!=[] or c != '0'):
                res.append(c*(counter[c]//2))
                counter[c] = counter[c]%2
        m = []
        for c in '9876543210':
            if counter[c]:
                m = [c]
                break;
                
        res = res + m + res[::-1]
        return ''.join(res)

                