class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        counter = Counter(nums)

        pair_count = 0
        for prefix in counter:
            if target.startswith(prefix):
                i = len(prefix)
                pair_count += counter[prefix] * counter[target[i:]]

                if prefix+prefix == target:
                    pair_count -= counter[prefix]
                    
        return pair_count