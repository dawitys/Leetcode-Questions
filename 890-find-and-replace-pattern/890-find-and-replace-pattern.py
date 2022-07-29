class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def match(word,pattern):
            mapping = {}
            for i in range(len(word)):
                if word[i] in mapping and mapping[word[i]] != pattern[i]:
                    return False
                elif word[i] not in mapping and pattern[i] in mapping.values():
                    return False
                
                mapping[word[i]] = pattern[i]
            return True
        
        ans = []
        for w in words:
            if match(w,pattern):
                ans.append(w)
                
        return ans