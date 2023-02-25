class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        def bounds(n):
            '''return the lower / upper bounds for number n'''
            if n % 2 == 1:
                n *= 2
            curr = n
            while curr & 1 == 0:
                curr >>= 1
            return curr, n
        
        nums = [(lower, upper) for lower, upper in map(bounds, nums)]
        heapq.heapify(nums)
        upper = max(x[0] for x in nums)
        lower = min(x[0] for x in nums)
        res = upper - lower
        while nums[0][0] < nums[0][1]:
            curr, mx = heapq.heappop(nums)
            heapq.heappush(nums, (curr * 2, mx))
            upper = max(upper, curr * 2)
            lower = nums[0][0]
            res = min(res, upper - lower)
        return res