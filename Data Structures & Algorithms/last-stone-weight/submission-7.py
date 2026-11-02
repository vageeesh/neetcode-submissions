class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # create max heap and remove first 2
        import heapq
        s = [-x for x in stones]
        heapq.heapify(s)
        while len(s) > 1:
            first = heapq.heappop(s)
            sec = heapq.heappop(s)
            if (first < sec):
                heapq.heappush(s, (first-sec))

        return -s[0] if s else 0


