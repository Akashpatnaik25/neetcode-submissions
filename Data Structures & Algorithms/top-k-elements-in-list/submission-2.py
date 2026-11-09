class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1
        res = [(key,val) for key, val in hashmap.items()]
        res.sort(key=lambda x: x[1])
        l = []
        for i in range(len(res)-1,len(res)-(k+1),-1):
            l.append(res[i][0])
        return l