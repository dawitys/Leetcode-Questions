class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ans = cnt = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                cnt += 1
            if i >= k and s[i - k] in 'aeiou':
                cnt -= 1
            ans  = max(cnt, ans)
        return ans 