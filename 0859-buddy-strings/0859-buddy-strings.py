class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        firstIndex = secondIndex = -1

        for i in range(len(s)):
            if s[i] != goal[i]:
                if firstIndex == -1:
                    firstIndex = i
                elif secondIndex == -1:
                    secondIndex = i
                else:
                    return False

        return secondIndex != -1 and s[firstIndex] == goal[secondIndex] and s[secondIndex] == goal[firstIndex]