class SegTree: 

    def __init__(self, arr: List[int]): 
        self.n = len(arr)
        self.tree = [0] * (2*self.n)
        # for i in range(2*self.n-1, 0, -1): 
        #     if i >= self.n: self.tree[i] = arr[i - self.n]
        #     else: self.tree[i] = max(self.tree[i<<1], self.tree[i<<1|1])

    def query(self, lo: int, hi: int) -> int: 
        ans = 0 
        lo += self.n 
        hi += self.n
        while lo < hi: 
            if lo & 1: 
                ans = max(ans, self.tree[lo])
                lo += 1
            if hi & 1: 
                hi -= 1
                ans = max(ans, self.tree[hi])
            lo >>= 1
            hi >>= 1
        return ans 

    def update(self, i: int, val: int) -> None: 
        i += self.n 
        self.tree[i] = val
        while i > 1: 
            self.tree[i>>1] = max(self.tree[i], self.tree[i^1])
            i >>= 1

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        m = max(nums)
        ans = 0 
        tree = SegTree([0] * (m+1))
        for x in nums: 
            val = tree.query(max(0, x-k), x) + 1
            ans = max(ans, val)
            tree.update(x, val)
        return ans 