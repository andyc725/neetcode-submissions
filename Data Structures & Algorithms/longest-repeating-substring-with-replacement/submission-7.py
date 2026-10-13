class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        #switch = k
        window = {}
        l = 0
        #r = 0

        '''
        for each window, check for the most frequent char
        save as a dict window
        if char != freq_max: replace the char && switch -= 1

        freq_max = max(window.value())
        if length - freq_max < k: okay to swicth
        else: l += 1, 
        '''

        #window[s[0]] = 1
        #for l in range(len(s)):
        #while r >= l and r < len(s):
        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            freq_max = max(window.values())
            length = (r - l) + 1
            while length - freq_max > k:
                window[s[l]] -= 1
                l += 1
                length = (r - l) + 1
            longest = max(longest, length)
    
            '''
            if s[r] == s[l]:
                freq_max = s[r]
                length = (r - l) + 1
                longest = max(longest, length)
                r += 1
            elif switch > 0:
                length = (r - l) + 1
                longest = max(longest, length)
                switch -= 1
                r += 1
            else:
                l += 1
                #r = l
                switch = k
            #switch = k
            '''

        return longest