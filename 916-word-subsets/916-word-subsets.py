class Solution:
    def wordSubsets(self, word1: List[str], word2: List[str]) -> List[str]:
        ans = []
        a = defaultdict(int)
        for w1 in word2:
            counter = Counter(w1)
            for c in counter:
                a[c] = max(a[c],counter[c])
            
        for w1 in word1:
            counter1 = Counter(w1)
            universal = True
            for c in a:
                if c not in counter1 or a[c] > counter1[c]:
                    universal = False
                    break
            
            if universal: 
                ans.append(w1)
                
        return ans