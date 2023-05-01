class Solution:
    def average(self, salary: List[int]) -> float:
        small, large, total, length = salary[0], salary[0], 0, 0
        for s in salary:
            total = total + s
            large = max(large, s)
            small = min(small, s)
            length = length + 1

        return (total - small - large)/(length - 2)