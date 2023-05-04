class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        RDRDDRRDD
        9
        [0,2,5,6,9]
        [1,3,4,7,8,10]
        '''
        rq = deque([i for i in range(len(senate)) if senate[i]=='R'])
        dq = deque([i for i in range(len(senate)) if senate[i]=='D'])
        
        while rq and dq:
            r,d = rq.popleft(),dq.popleft()
            if r>d:
                dq.append(len(senate)+d)
            else:
                rq.append(len(senate)+r)
                
        return 'Radiant' if rq else 'Dire'