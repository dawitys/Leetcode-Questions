def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        pairs = 0
        first_digits = [0]*10
        for i in range(len(nums)):
            for j in range(1,10):
                if gcd(nums[i]%10,j) ==1:
                    pairs += first_digits[j]
                    
            n = nums[i]
            while n >=10:
                n //= 10
            first_digits[n] += 1
        
        return pairs