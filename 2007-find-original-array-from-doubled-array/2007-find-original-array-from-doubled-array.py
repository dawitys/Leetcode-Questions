class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        res = []
        counter = defaultdict(int)

        changed.sort()
        for num in changed:
            if num % 2 == 0 and counter[num/2] > 0:
                counter[num/2] -= 1
                res.append(num/2)
            else:
                counter[num] += 1
        
        for n in counter:
            if counter[n] > 0:
                return []
        
        return res