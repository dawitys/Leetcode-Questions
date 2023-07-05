class Solution:
    def longestSubarray(self, A: List[int]) -> int:
        k = 1
        i = 0
        for j in range(len(A)):
            k -= A[j] == 0
            if k < 0:
                k += A[i] == 0
                i += 1
        return j - i