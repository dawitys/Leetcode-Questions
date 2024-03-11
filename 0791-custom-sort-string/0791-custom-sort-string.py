class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        alp = []
        for c in s:
            if c in order:
                alp.append(c)
            else:
                res.append(c)
        alp.sort(key = lambda  c : order.index(c))
        res = alp + res
        return ''.join(res)