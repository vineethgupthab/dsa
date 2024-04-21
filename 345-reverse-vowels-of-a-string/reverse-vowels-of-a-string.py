class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0; right = len(s)-1
        vowels = 'aeiou'
        s=list(s)
        while left<right:
            if s[left].lower() not in vowels:
                left+=1
                continue
            if s[right].lower() not in vowels:
                right-=1
                continue
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return ''.join(s)