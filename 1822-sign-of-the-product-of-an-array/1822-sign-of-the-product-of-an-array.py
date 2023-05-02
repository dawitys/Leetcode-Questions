class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for n in nums:
            product *= n
        return product//abs(product) if product != 0 else 0