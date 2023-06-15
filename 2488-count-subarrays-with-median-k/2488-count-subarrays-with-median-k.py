class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
        '''
        sub array - litrally part of the array itself
        sub sequence, some elements can be dropped while considering the newly created array
        
        3
        5
        
        '''
        balance = [0]*len(nums)
        
        for i in range(len(nums)):
            if nums[i] < k:
                balance[i] = -1
            if nums[i] > k:
                balance[i] = 1
                
        k_pos = nums.index(k)
        ans=0
        mapping = defaultdict(int)
        runn = 0
        for i in range(k_pos,len(nums)):
            runn += balance[i]
            if runn == 0 or runn == 1:
                ans += 1
            mapping[runn] += 1
        runn = 0
        for i in range(k_pos-1,-1,-1):
            runn += balance[i]
            ans += mapping[-runn]
            ans += mapping[-runn+1]
            
        
        return ans