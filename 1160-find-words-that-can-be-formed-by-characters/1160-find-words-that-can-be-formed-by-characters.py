class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            can = True
            char = Counter(chars)
            freq = Counter(word)
            for c in freq:
                if freq[c] > char[c]:
                    can = False
                    break
                char[c] -= freq[c]
            if can:
                count += len(word)
                
        return count