class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h_map={}
        for key in nums:
            if key in h_map:
                h_map[key]=h_map[key]+1
            else:
                h_map[key]=1
        result=sorted(h_map,key=lambda x:h_map[x],reverse=True)
        return result[:k]