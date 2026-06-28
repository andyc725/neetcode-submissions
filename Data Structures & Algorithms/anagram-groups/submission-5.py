class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        d = {}
        for s in strs:
            key = list()
            for i in range(len(s)):
                key.append(s[i])
            key.sort()
            key = tuple(key)
            if key in d.keys():
                d[key].append(s)
            else:
                d[key] = [s]
        
        return list(d.values())