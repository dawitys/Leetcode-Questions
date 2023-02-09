class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ips = []
        def dfs(path,idx):

            if len(path) == 4 and idx == len(s):
                ips.append('.'.join(path))
                return
            if idx >= len(s):
                return
            dfs(path + [s[idx:idx+1]],idx + 1)
            
            if idx < len(s) - 1 and s[idx] != '0'  :
                dfs(path + [s[idx:idx+2]],idx + 2)
            
            if idx < len(s) - 2 and s[idx] != '0' and int(s[idx:idx+3]) <= 255  :
                dfs(path + [s[idx:idx+3]],idx + 3)
                
                
        dfs([],0)
        return ips