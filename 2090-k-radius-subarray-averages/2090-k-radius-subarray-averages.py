class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        averages = [-1]*len(nums)
        running_sum = sum(nums[:2*k +1])
        
        for i in range(k,len(nums)-k):
            averages[i] = running_sum//(2*k+1)
            running_sum -= nums[i-k]
            running_sum += nums[i+k+1] if i+k+1 < len(nums) else 0
            
        return averages