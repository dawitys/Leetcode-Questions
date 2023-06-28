class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)                        
        sub_arrays = set()
        
        for start in range(n):
            cnt = 0
            temp = ''
            for i in range(start, n):
                if nums[i]%p == 0:
                    cnt+=1                 
                temp+=str(nums[i]) + ','          
                if cnt>k:
                    break
                sub_arrays.add(temp)                                    
                
        return len(sub_arrays)