class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        
        for key,value in hashmap.items():
            if n <= value :
                return key
        return 0
