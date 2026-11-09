class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_pos = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

        n = len(nums) - 1
        while n >= 0 and nums[n] == val:
            nums.pop()
            n -= 1
            
        return len(nums)