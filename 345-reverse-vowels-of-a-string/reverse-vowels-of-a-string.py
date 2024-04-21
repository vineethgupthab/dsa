class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0; right = len(s)-1
        vowels = 'aeiou'
        s=list(s)
        while left<right:
            if s[left].lower() not in vowels:
                left+=1
            if s[right].lower() not in vowels:
                right-=1
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return ''.join(s)