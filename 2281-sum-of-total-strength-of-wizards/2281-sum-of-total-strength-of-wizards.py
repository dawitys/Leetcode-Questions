class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        mod, n = 10 ** 9 + 7, len(strength)
        
        # Get the first index of the smaller value to strength[i]'s right.
        right_index = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] >= strength[i]:
                right_index[stack.pop()] = i
            stack.append(i)

        # Get the first index of the smaller value to strength[i]'s left.
        left_index = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[i]:
                left_index[stack.pop()] = i
            stack.append(i)
            
        # prefix sum of the prefix sum array of strength.
        presum_of_presum =  list(accumulate(accumulate(strength), initial = 0))
        answer = 0
        
        # For each element in strength, we get the value of R_term - L_term.
        for i in range(n):
            # Get the left index and the right index.
            left_bound = left_index[i]
            right_bound = right_index[i]
            
            # Get the left_count and right_count (marked as L and R in the picture)
            left_count = i - left_bound
            right_count = right_bound - i
            
            # Get positive presum and the negative presum
            neg_presum = presum_of_presum[i] - presum_of_presum[max(left_bound, 0)]
            pos_presum = presum_of_presum[right_bound] - presum_of_presum[i]
            
            # The part having strength[i] as the minimum values equals
            # strength[i] multiply by (pos_presum - neg_presum)
            answer += strength[i] * (pos_presum * left_count - neg_presum * right_count)
            
        return answer % mod