class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def match(word):
            mapping = {}
            for i in range(len(word)):
                if word[i] in mapping and mapping[word[i]] != pattern[i]:
                    return False
                
                mapping[word[i]] = pattern[i]
                
            return len(set(mapping.values())) == len(mapping.values())
                
        return filter(match,words)