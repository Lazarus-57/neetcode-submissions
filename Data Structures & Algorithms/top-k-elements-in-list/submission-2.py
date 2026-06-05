class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        for i in nums:
            if i in h_map:
                h_map[i]=h_map[i]+1
            else:
                h_map[i]=1
        result=sorted(h_map,key=lambda x:h_map[x],reverse=True)
        return result[:k]
