class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        position = {}
        for i,c in enumerate(order):
            position[c] = i
            
        for i in range(1,len(words)):
            prev,curr = words[i-1],words[i]
            P,C = len(prev),len(curr)
            idx = 0
            while idx < min(P,C) and prev[idx] == curr[idx]:
                idx += 1

            
            if (idx >= min(P,C) and  C < P ):
                return False
            
            if idx < min(P,C) and position[prev[idx]] > position[curr[idx]] :
                return False
            
        return True