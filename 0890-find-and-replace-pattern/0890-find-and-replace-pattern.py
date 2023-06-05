class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def encode(word):
            mapping = {}
            i = 0
            encode = []
            
            for w in word:
                if w not in mapping:
                    mapping[w] = i
                    i += 1
                encode.append(mapping[w])
            return encode
        
        ans = []
        pattern_encoding = encode(pattern)
        for word in words:
            
            word_encoding = encode(word)
            
            if word_encoding == pattern_encoding:
                ans.append(word)
                
        return ans