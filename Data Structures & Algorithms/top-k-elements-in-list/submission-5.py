class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            elif i in hashmap:
                hashmap[i]+=1
        #This is already O(n) time complexity
        #Now how do we return the top k most frequent elements?
                
        return sorted(hashmap, key=lambda x: hashmap[x], reverse=True)[:k]