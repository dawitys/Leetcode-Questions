class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        total = 0
        max_frequency = -float('inf')
        
        frequencies = Counter(nums)
        
        for elt in frequencies:
            if frequencies[elt] > max_frequency:
                max_frequency = frequencies[elt]
                total = frequencies[elt]
            elif frequencies[elt] == max_frequency:
                total += frequencies[elt]
        return total