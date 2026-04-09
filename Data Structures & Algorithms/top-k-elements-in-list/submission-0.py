class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)

        # use min heap approach
        # minHeap = []
        
        # for n, freq in frequencies.items():
        #     heapq.heappush(minHeap, (freq, n))

        #     if len(minHeap) > k:
        #         heapq.heappop(minHeap)

        #     print(minHeap)

        # return [num for freq, num in minHeap]

        # use bucket sort approach
        bucket = [[] for i in range(len(nums) + 1)]

        for num, freq in frequencies.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res
