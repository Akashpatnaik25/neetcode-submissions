class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq_count = {}

        for i in range(len(nums)):
            # check if the required difference is in set or not
            diff = target - nums[i]
            if diff in freq_count:
                return [freq_count[diff], i]

            # Store current number for future lookups
            freq_count[nums[i]] = i

        return [0, 0]
            
        