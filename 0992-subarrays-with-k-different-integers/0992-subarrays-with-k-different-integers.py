class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        counter1 = Counter()
        counter2 = Counter()
        slow = fast = res = 0

        for n in nums:
            counter1[n], counter2[n] = counter1[n] + 1, counter2[n] + 1
            while len(counter2) == k:
                counter2[nums[fast]] -= 1
                if counter2[nums[fast]] == 0: 
                    del counter2[nums[fast]]
                fast += 1
            while len(counter1) > k:
                counter1[nums[slow]] -= 1
                if  counter1[nums[slow]] == 0: 
                    del counter1[nums[slow]]
                slow += 1
                
            res += fast - slow

        return res