class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        for idea in ideas:
            groups[ord(idea[0]) - ord('a')].add(idea[1:])
        
        ans = 0
        for i in range(25):
            for j in range(i + 1, 26):
                k = len(groups[i] & groups[j])
                ans += 2 * (len(groups[i]) - k) * (len(groups[j]) - k)
        return ans