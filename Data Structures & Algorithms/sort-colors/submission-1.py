class Solution:
    def sort(self,left,right):
        
        l = len(left)
        r = len(right)
        i = j = 0
        result = []
        while i < l and j < r:
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result
            

    def merge(self,arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr)//2
        left = self.merge(arr[:mid])
        right = self.merge(arr[mid:])
        return self.sort(left,right)

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = self.merge(nums)
        return nums