class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        freq_map = [[] for i in range(len(nums) + 1)]
        max_freq = float("-inf")

        for num, freq in count.items():
            max_freq = max(freq, max_freq)

            freq_map[freq].append(num)
            
        res = []

        for i in range(len(freq_map) - 1, -1, -1):
            for num in freq_map[i]:
                res.append(num)
                if len(res) == k:
                    return res
