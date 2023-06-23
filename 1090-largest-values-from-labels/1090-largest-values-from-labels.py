class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        
        count = score = 0
        seen = defaultdict(int)
        
        for n in sorted(zip(values,labels),reverse=True):
            if count >= numWanted:
                break
            if seen[n[1]] >= useLimit or (len(seen)>=numWanted and n[1] not in seen):
                continue
            
            score += n[0]
            seen[n[1]] += 1
            count += 1
            
        return score