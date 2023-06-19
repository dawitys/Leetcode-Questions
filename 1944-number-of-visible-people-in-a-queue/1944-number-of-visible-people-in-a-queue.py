class Solution:
    def canSeePersonsCount(self, nums: List[int]) -> List[int]:

        N = len(nums)
        Stack = []
        Ans = [0]*N
        for i in range(N-1,-1,-1):
            while Stack and Stack[-1] < nums[i]:
                Ans[i] += 1
                Stack.pop()
            if Stack:
                Ans[i] += 1
            Stack.append(nums[i])

        return Ans