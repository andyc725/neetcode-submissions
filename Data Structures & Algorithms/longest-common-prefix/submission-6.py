class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(200):
            count = 0
            for j in strs:
                if len(j) == 0:
                    return ""
                elif j[i] != strs[0][i]:
                    return res
                elif len(j) - 1 == i:
                    count += 1
                #    res = res + strs[0][i]
                #    return res
            res = res + strs[0][i]
            if count >= 1:
                return res
        return res