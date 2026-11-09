class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j = 0,1
        while j < (len(nums)) :
            print(nums[i],nums[j])
            if nums[i] == nums[j] :
                nums[i] = "_"
            i += 1
            j += 1
        nums[:] = [i for i in nums if i != "_"]
        return len(nums)