class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_count = {}

        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1


        for num in freq_count:
            if freq_count[num] > 1:
                return True

        return False