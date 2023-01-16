class Solution:
    def countTime(self, time: str) -> int:
        ans = 1
        
        for i,c in enumerate(time):
            if c == '?':
                if (i == 1 and time[0] in '01?') or i == 4:
                    ans *= 10

                if (i == 3):
                    ans *= 6
        
                if i == 1 and time[0]=='2':
                    ans *= 4  

        if time[0] == '?':
            if time[1] in '0123':
                ans = ans * 3  
            elif time[1] == '?':
                ans = (2*ans//5) + ( 2* ans)
            else:
                ans *= 2

        return ans
                    