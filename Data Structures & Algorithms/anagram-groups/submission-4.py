class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        
        output = list()
        key = list()
        for w in strs:
            countW = {}
            for i, n in enumerate(w):
                countW[w[i]] = 1 + countW.get(w[i], 0)
            
            if key.count(countW) == 0:
                key.append(countW)
                output.append([w])
            else:
                index = key.index(countW)
                output[index].append(w)
        
        return output
            
  
