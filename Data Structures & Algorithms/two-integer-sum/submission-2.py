class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = 0
        l = []
        i = 0
        length = len(nums)
        while i < length:
            j = i+1
            point = nums[i]
            temp = target - point
            while j < length:
                if nums[j] == temp:
                    return [i,j]
                j+=1
            i+=1
        return [0,1]
