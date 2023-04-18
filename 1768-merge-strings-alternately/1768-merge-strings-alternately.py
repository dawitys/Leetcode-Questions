class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        shortest = min(len(word1),len(word2))
        return ''.join([word1[i]+word2[i] for i in range(shortest)]) + word1[shortest:]+word2[shortest:]