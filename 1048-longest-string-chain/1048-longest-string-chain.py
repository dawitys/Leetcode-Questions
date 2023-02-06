class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words_set = set(words)
        
        cache = {}
        def dp(word,cache):
            if word in cache:
                return cache[word]
            res = 0
            for i in range(len(word)):
                temp_word = word[:i] + word[i+1:]
                if temp_word in words_set:
                    res = max(res, dp(temp_word,cache))
            cache[word] = res + 1
            return res + 1
        
        cache = {}
        ans = 0
        for word in words:
            ans = max(ans, dp(word,cache))
        
        return ans