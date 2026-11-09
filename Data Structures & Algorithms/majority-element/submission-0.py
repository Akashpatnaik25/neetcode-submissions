class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from math import ceil
        from collections import Counter
        l = ceil(len(nums)/2)
        freq = Counter(nums)

        for key, value in freq.items():
            if value >=l:
                return key
        return -1
