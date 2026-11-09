class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        first we will store the frequency count,
        and sort and then k fill get the result 
        """
        freq_dict = dict()
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i,0)
        # bucket sort
        sort_by_values = [[] for _ in range(len(nums)+1)]
        for key, value in freq_dict.items():
            if key in freq_dict:
                sort_by_values[freq_dict[key]].append(key) 
        print(sort_by_values)
        res = []
        for i in range(len(sort_by_values)-1, -1, -1 ):
            if sort_by_values[i]:
                for j in sort_by_values[i]:
                    res.append(j)
                    if len(res) == k:
                        return res
        return res