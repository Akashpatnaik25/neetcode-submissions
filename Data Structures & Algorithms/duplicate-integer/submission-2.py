class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_count = {}

        # frequency count for each element
        for num in nums:
            freq_count[num] = freq_count.get(num, 0) + 1

        # frequency count exceeds 1 means there a duplicate
        for num in freq_count:
            if freq_count[num] > 1:
                return True

        # no-duplicate found
        return False