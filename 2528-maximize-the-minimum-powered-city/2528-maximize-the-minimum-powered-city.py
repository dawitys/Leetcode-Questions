class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        def isGood(minPowerRequired, additionalStations):
            windowPower = sum(stations[:r])
            additions = [0] * n
            for i in range(n):
                if i + r < n:
                    windowPower += stations[i + r]

                if windowPower < minPowerRequired:
                    needed = minPowerRequired - windowPower
                    if needed > additionalStations:
                        return False
                    additions[min(n - 1, i + r)] += needed
                    windowPower = minPowerRequired
                    additionalStations -= needed

                if i - r >= 0:
                    windowPower -= stations[i - r] + additions[i - r]

            return True

        left = 0
        right = sum(stations) + k  
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if isGood(mid, k):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans