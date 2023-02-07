class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        temp, tempLength, res = [], 0, []
        
        for word in words:
            if len(word) + tempLength + len(temp) - 1 >= maxWidth:
                free = maxWidth - tempLength
                count_spaces = len(temp) - 1
                
                for i in range(len(temp)):
                    w = temp[i]
                    wordSpace = free if count_spaces == 0 else math.ceil(free/count_spaces)
                    temp[i] = temp[i] + ''.join([' '] * wordSpace)
                    
                    free -= wordSpace
                    count_spaces -= 1
                    
                res.append(''.join(temp))
                temp, tempLength = [], 0
                
            temp.append(word)
            tempLength += len(word)
            
        temp = ' '.join(temp)
        
        if len(temp) < maxWidth:
            temp = temp + ''.join([' '] * (maxWidth - len(temp)))
        
        res.append(temp)
        
        return res 