class Solution:
    def minDeletions(self, s: str) -> int:
        '''
        1 3 4 5 5
        
        '''
        counter = Counter(s)
        freqs = sorted([counter[k] for k in counter],reverse = True)
        
        steps = 0
        seen = set()
        for i in range(len(freqs)):
            while(freqs[i] in seen):
                freqs[i] -= 1
                steps += 1
                if freqs[i] == 0:
                    break
            if freqs[i] != 0:
                seen.add(freqs[i])
            
            
        return steps