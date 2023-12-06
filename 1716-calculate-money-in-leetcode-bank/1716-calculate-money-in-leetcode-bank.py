class Solution:
    def totalMoney(self, n: int) -> int:
        if n <= 7:
            return n * (n+1)//2

        weeks = n // 7
        total = weeks * 28
        # Sum of AP
        total += (weeks*(weeks-1)*7)//2

        if n % 7 != 0:
            days = n % 7
            day = weeks+1
            for j in range(days):
                total += day
                day += 1

        return total