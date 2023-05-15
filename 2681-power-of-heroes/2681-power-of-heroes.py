class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        nums.sort()
        prev = ans = 0
        mod = 10**9 + 7

        for i in range(len(nums)):
            power = nums[i] * nums[i]
            ans += prev * power
            prev = prev * 2 + nums[i]

            
        ans += sum([n**3 for n in nums])
            

        return ans % mod
