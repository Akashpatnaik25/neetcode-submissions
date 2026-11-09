class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        first we will store the frequency count,
        and sort and then k fill get the result 
        """
        freq_dict = dict()
        for i in nums:
            freq_dict[i] = 1 + freq_dict.get(i,0)
        
        sort_by_values = sorted(freq_dict.items(), key=lambda x: x[1],reverse=True)
        res = []
        for i in range(k):
            res.append(sort_by_values[i][0])
        return res