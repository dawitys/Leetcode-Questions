class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: 
            return 'Zero'
        
        numToWord = {
            '0':['','',''],
            '1':['One','','One Hundred'],
            '2':['Two','Twenty','Two Hundred'],
            '3':['Three','Thirty','Three Hundred'],
            '4':['Four','Forty','Four Hundred'],
            '5':['Five','Fifty','Five Hundred'],
            '6':['Six','Sixty','Six Hundred'],
            '7':['Seven','Seventy','Seven Hundred'],
            '8':['Eight','Eighty','Eight Hundred'],
            '9':['Nine','Ninety','Nine Hundred'],
        }
        specials = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        multipliers = ['','Thousand','Million','Billion']
        ans = []
        num_str = str(num)
        multiplier = 0
        for i in range(len(num_str)-3,-3,-3):
            sub = num_str[i:i+3]
            if i < 0:
                sub = num_str[:i+3]
            temp = []
            if len(sub) > 1 and sub[-2] == '1':
                temp = [numToWord[sub[-3]][2]] + [specials[int(sub[-1])]] if len(sub)>2 else [specials[int(sub[-1])]]
            else:
                for j in range(len(sub)-1,-1,-1):
                    temp = [numToWord[sub[j]][len(sub)-1-j]] + temp
            ans = temp + [multipliers[multiplier]] + ans if ''.join(temp)!='' else ans
            multiplier += 1
            
        return ' '.join([w for w in ans if w!=''])