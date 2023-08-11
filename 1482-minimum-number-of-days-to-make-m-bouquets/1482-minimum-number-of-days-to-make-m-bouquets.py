class Solution:
    def binarySearch(self,left, right, bloomDay, m, k):

        minDays = float('inf')

        while left <= right:
            mid = left + (right-left) // 2

            bouqet = 0
            flower = 0

            for bloom in bloomDay:

                if bloom <= mid:
                    flower += 1
                else:
                    flower = 0
                if flower == k:
                    bouqet += 1
                    flower = 0

            if bouqet >= m:
                minDays = min(minDays, mid)  
                right = mid - 1
            else:
                left = mid + 1

        return minDays    

    def minDays(self,bloomDay, m, k):

        n = len(bloomDay)

        if m * k > n:
            return -1

        min_  = min(bloomDay)
        max_ = max(bloomDay)

        answer = self.binarySearch(min_, max_, bloomDay, m, k)

        return answer





