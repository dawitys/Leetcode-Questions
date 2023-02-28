class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left  = {n:nums.index(n) for n in nums}
        right = {}
        count = defaultdict(int)
        for i in range(len(nums)):
            right[nums[i]] = i
            count[nums[i]] += 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans