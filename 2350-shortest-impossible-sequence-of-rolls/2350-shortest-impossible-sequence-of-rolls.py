
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        seen = set()
        
        possible = 0
        for i in range(len(rolls)-1,-1,-1):
            seen.add(rolls[i])
            if len(seen) ==k:
                possible += 1
                seen = set()
        return possible +1

        
        