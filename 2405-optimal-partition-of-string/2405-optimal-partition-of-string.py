class Solution:
    def partitionString(self, s: str) -> int:
        mask = partitions = 0
        for c in s:
            if mask & 1<<(ord(c)-ord('a')):
                partitions += 1
                mask = 0
            mask |= 1<<(ord(c)-ord('a'))

        return partitions + 1