class Solution:
    def minDistance(self, s1: str, s2: str) -> int:

        @lru_cache(maxsize=None)
        def f(i, j):
            if i == 0 and j == 0: return 0
            if i == 0 or j == 0: return i or j
            if s1[i - 1] == s2[j - 1]:
                return f(i - 1, j - 1)
            return min(1 + f(i, j - 1), 1 + f(i - 1, j), 1 + f(i - 1, j - 1))

        m, n = len(s1), len(s2)
        return f(m, n)