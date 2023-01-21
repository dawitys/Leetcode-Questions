class Solution:
    def maximumWhiteTiles(self, T: List[List[int]], clen: int) -> int:
        T.sort()
        pref = [0] + list(itertools.accumulate(r - l + 1 for l, r in T))
        ends = [r for _, r in T]
        
        n = len(ends)
        j, ans = 0, 0
        
        for i in range(n):
            l, _ = T[i]                        # Carpet starts from the begining of each range
            r = min(ends[-1], l + clen - 1)    # The rightmost index having tile is ends[-1]

            while j < n and ends[j] < r:       # While the WHOLE current range is covered by carpet
                j += 1
            
            # Two cases: 
            if T[j][0] > r:    # If the right end of the carpet doesn't reach the j-th range.
                ans = max(ans, pref[j] - pref[i])
            else:              # If the right end of the carpet covers part of the j-th range.
                ans = max(ans, pref[j + 1] - pref[i] - ends[j] + r)
            
        return ans
        
        