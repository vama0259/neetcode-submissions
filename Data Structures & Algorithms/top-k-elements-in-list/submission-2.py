class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i] = 1
        
        return sorted(a, key=a.get, reverse = True)[:k]
        