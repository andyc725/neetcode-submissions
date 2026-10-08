class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()

        for r in range(len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                w = (r - l) + 1
                longest = max(longest, w)
            else: 
                while s[r] != s[l] and r >= l:
                    seen.remove(s[l])
                    l += 1
                if s[r] == s[l]:
                    l += 1
            
        return longest    


        