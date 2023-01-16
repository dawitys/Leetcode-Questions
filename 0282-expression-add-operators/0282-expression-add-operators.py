class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:

        def backtrack(idx=0, path='', value=0, prev=None):            
            if idx == len(num) and value == target:
                rtn.append(path)
                return
            
            for i in range(idx+1, len(num) + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    if prev is None :
                        backtrack(i, num[idx: i], tmp, tmp)
                    else:
                        backtrack(i, path+'+'+num[idx: i], value + tmp, tmp)
                        backtrack(i, path+'-'+num[idx: i], value - tmp, -tmp)
                        backtrack(i, path+'*'+num[idx: i], value - prev + prev*tmp, prev*tmp)
        
        rtn = []
        backtrack()
        
        return rtn