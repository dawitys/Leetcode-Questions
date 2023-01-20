class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        '''
        abcc
        aab
        '''
        w1_chars,w2_chars = [0]*26,[0]*26
        
        for w in word1:
            w1_chars[ord(w)-ord('a')] += 1
            
        for w in word2:
            w2_chars[ord(w)-ord('a')] += 1
        print(w1_chars,w2_chars)
        for i in range(26):
            for j in range(26):
                if w1_chars[i]>0 and w2_chars[j]>0:
                    w1_chars[i] -= 1
                    w1_chars[j] += 1
                    w2_chars[j] -= 1
                    w2_chars[i] += 1

                    w1 = w2 = 0
                    for idx in range(26):
                        if w1_chars[idx]:
                            w1 += 1
                        if w2_chars[idx]:
                            w2 += 1
                    if w1==w2:
                        return True

                    w1_chars[i] += 1
                    w1_chars[j] -= 1
                    w2_chars[j] += 1
                    w2_chars[i] -= 1
                    
                
        return False
                
