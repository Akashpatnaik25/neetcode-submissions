class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        start, end = 0, len(nums)

        while start < end:
            if nums[start] + nums[end] == target:
                return [start, end]
            elif 
        '''

        freq_count = {}

        for i in range(len(nums)):
            diff_exist = target - nums[i]
            if diff_exist in freq_count:
                return [freq_count[diff_exist], i]

            freq_count[nums[i]] = i

        return [0, 0]
            
        