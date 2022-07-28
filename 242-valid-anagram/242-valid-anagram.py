class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(t)
        
        for c in counter1:
            if c not in counter2 or counter2[c] != counter1[c]:
                return False
            
        for c in counter2:
            if c not in counter1 or counter2[c] != counter1[c]:
                return False
            
        return True