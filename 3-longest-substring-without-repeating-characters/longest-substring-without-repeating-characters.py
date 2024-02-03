class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_string = ''; max_len = 1
        if len(s) <= 1:
            return len(s)
        else:
            for i in range(len(s)):
                sub_string = s[i]
                for j in range(i+1,len(s)):
                    if s[j] not in sub_string:
                        sub_string+=s[j]
                        if max_len<len(sub_string):
                            max_len = len(sub_string)
                    else:
                        break
        return max_len