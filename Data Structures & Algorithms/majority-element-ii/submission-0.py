class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = dict()
        for i in nums:
            freq[i] = freq.get(i,0) + 1
        res = []
        for key,val in freq.items():
            if len(nums)//3 < val :
                res.append(key)

        return res 