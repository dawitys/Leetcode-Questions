class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        char = Counter(chars)
        for word in words:
            can = True
            freq = Counter(word)
            for c in freq:
                if freq[c] > char[c]:
                    can = False
                    break

            if can:
                count += len(word)
                
        return count