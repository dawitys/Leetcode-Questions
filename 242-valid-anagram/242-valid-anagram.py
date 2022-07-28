class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 27
        for i, j in zip_longest(s, t, fillvalue='{'):
            letters[ord(i) - 97] += 1
            letters[ord(j) - 97] -= 1
        return any(letters) is False