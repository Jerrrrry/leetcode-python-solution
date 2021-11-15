class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits=collections.deque([])
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.hits.append(timestamp)
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.hits)>0 and timestamp-self.hits[0]>=300:
            self.hits.popleft()
        return len(self.hits)
