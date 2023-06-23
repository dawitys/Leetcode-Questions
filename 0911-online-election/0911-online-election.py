from sortedcontainers import SortedDict

class TopVotedCandidate:
    def __init__(self, persons, times):
            self.leads, self.times, count = [], times, defaultdict(int)
            lead = -1
            for p in persons:
                count[p] = count[p] + 1
                if count[p] >= count[lead]: 
                    lead = p
                self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)