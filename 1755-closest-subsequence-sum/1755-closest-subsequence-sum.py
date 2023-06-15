class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        def dfs(i,cur,arr,sums):
            if i==len(arr):
                sums.add(cur)
                return
            dfs(i+1,cur,arr,sums)
            dfs(i+1,cur+arr[i],arr,sums)
        
        sums1,sums2=set(),set()
        dfs(0,0,nums[:len(nums)//2],sums1)
        dfs(0,0,nums[len(nums)//2:],sums2)
        

        s2=sorted(sums2)
        ans=10**10
        for s in sums1:
            remain=goal-s
            i2=bisect_left(s2,remain)
            if i2<len(s2):
                ans=min(ans,abs(remain-s2[i2]))
            if i2>0:
                ans=min(ans,abs(remain-s2[i2-1]))
        return ans