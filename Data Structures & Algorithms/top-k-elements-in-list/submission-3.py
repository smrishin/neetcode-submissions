class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # max Heap
        maxh = []
        count = Counter(nums)

        for num, freq in count.items():
            heapq.heappush(maxh, (-freq, num))

        res = []

        while maxh and len(res) < k:
            res.append(heapq.heappop(maxh)[1])
        return res


        # min Heap
        minh = []
        count = Counter(nums)

        for num, freq in count.items():
            heapq.heappush(minh, (freq, num))
            if len(minh) > k:
                heapq.heappop(minh)
        res = []

        while minh:
            res.append(heapq.heappop(minh)[1])
        return res

        # # Sorting
        # count = Counter(nums)

        # freq_arr = []
        # for num, freq in count.items():
        #     freq_arr.append((freq, num))
        # freq_arr.sort()

        # res = []

        # while len(res) < k:
        #     res.append(freq_arr.pop()[1])
        # return res


        # # Bucket sort
        # count = Counter(nums)

        # freq_map = [[] for i in range(len(nums) + 1)]
        # max_freq = float("-inf")

        # for num, freq in count.items():
        #     max_freq = max(freq, max_freq)

        #     freq_map[freq].append(num)
            
        # res = []

        # for i in range(len(freq_map) - 1, -1, -1):
        #     for num in freq_map[i]:
        #         res.append(num)
        #         if len(res) == k:
        #             return res
