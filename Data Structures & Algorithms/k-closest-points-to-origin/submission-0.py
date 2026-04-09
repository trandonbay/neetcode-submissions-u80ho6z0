class Solution:
    def eu_dist(self, x, y):
        return math.sqrt((x**2) + (y**2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(self.eu_dist(x, y), [x,y]) for x, y in points]
        heapq.heapify(distances)

        res = []
        while k:
            res.append(heapq.heappop(distances)[1])
            k -= 1

        return res