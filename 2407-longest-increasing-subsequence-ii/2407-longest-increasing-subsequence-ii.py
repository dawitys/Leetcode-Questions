
class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        
        ml=[[] for i in range(6)]
        ml[0]=1
        ml[1]=[0]*11
        ml[2]=[0]*101
        ml[3]=[0]*1001
        ml[4]=[0]*10001
        ml[5]=[0]*100001
        
        n=nums[0]
        ml[5][n]=1
        ml[4][n//10]=1
        ml[3][n//100]=1
        ml[2][n//1000]=1
        ml[1][n//10000]=1
        for n in nums[1:]:
            pos1=max(0, n-k)
            mx=0
            for i in range((pos1-1)//10000+1, n//10000):
                if ml[1][i]>mx:
                    mx=ml[1][i]
            if k//10000>1:
                for i in range((pos1-1)//1000+1, ((pos1-1)//10000+1)*10):
                    if ml[2][i]>mx:
                        mx=ml[2][i]
                for i in range((n//10000)*10, n//1000):
                    if ml[2][i]>mx:
                        mx=ml[2][i]
            else:
                for i in range((pos1-1)//1000+1, n//1000):
                    if ml[2][i]>mx:
                        mx=ml[2][i]
            if k//1000>1:
                for i in range((pos1-1)//100+1, ((pos1-1)//1000+1)*10):
                    if ml[3][i]>mx:
                        mx=ml[3][i]
                for i in range((n//1000)*10, n//100):
                    if ml[3][i]>mx:
                        mx=ml[3][i]
            else:
                for i in range((pos1-1)//100+1, n//100):
                    if ml[3][i]>mx:
                        mx=ml[3][i]
            if k//100>1:
                for i in range((pos1-1)//10+1, ((pos1-1)//100+1)*10):
                    if ml[4][i]>mx:
                        mx=ml[4][i]
                for i in range((n//100)*10, n//10):
                    if ml[4][i]>mx:
                        mx=ml[4][i]
            else:
                for i in range((pos1-1)//10+1, n//10):
                    if ml[4][i]>mx:
                        mx=ml[4][i]
            if k//10>1:
                for i in range(pos1, ((pos1-1)//10+1)*10):
                    if ml[5][i]>mx:
                        mx=ml[5][i]
                for i in range((n//10)*10, n):
                    if ml[5][i]>mx:
                        mx=ml[5][i]
            else:
                for i in range(pos1, n):
                    if ml[5][i]>mx:
                        mx=ml[5][i]
            mx+=1
            if mx>ml[5][n]:
                ml[5][n]=mx
            if mx>ml[4][n//10]:
                ml[4][n//10]=mx
            if mx>ml[3][n//100]:
                ml[3][n//100]=mx
            if mx>ml[2][n//1000]:
                ml[2][n//1000]=mx
            if mx>ml[1][n//10000]:
                ml[1][n//10000]=mx
            if mx>ml[0]:
                ml[0]=mx
        return ml[0]