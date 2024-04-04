class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        common = ''
        min_length = min(len(str1), len(str2))
        
        for i in range(1, min_length + 1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                substr = str1[:i]
                if substr * (len(str1) // i) == str1 and substr * (len(str2) // i) == str2:
                    common = substr
                    
        return common