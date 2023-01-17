class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        idx = 0
        while True:
            for i in range(len(strs)):
                if len(strs[i]) <= idx or strs[i][idx] != strs[0][idx]:
                    return strs[0][:idx]

            idx += 1
            
        return strs[0][:idx]