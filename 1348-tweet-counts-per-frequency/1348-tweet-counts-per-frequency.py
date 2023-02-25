from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(SortedList)
        self.window = {"minute": 60, "hour": 3600, "day":86400}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)
            
    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        res = [0] * ((endTime - startTime) // self.window[freq] + 1)
        start_idx = bisect_left(self.tweets[tweetName],startTime)
        end_idx =bisect_right(self.tweets[tweetName],endTime)
        
        for i in range(start_idx, end_idx):
            time = (self.tweets[tweetName][i] - startTime) // self.window[freq]
            res[time] += 1
            
        return res

# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)