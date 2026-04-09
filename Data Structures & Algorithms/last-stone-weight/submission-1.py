class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x, y = -heapq.heappop(maxHeap), -heapq.heappop(maxHeap)
            diff = x - y

            if diff > 0:
                heapq.heappush(maxHeap, -diff)
            elif diff < 0:
                heapq.heappush(maxHeap, diff)

        return -maxHeap[0] if len(maxHeap) else 0