class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map={}
        for i in strs:
            key=tuple(sorted(i))
            if key in h_map:
                h_map[key].append(i)
            elif key not in h_map:
                h_map[key]=[i]
        return list(h_map.values())