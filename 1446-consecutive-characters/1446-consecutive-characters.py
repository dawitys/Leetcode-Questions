class Solution:
    def maxPower(self, s: str) -> int:
        power = 1
        curr_power = 1
        
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                curr_power += 1
            else:
                power = max(power,curr_power)
                curr_power = 1
                
        return max(power,curr_power)