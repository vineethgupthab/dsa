class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1)<len(word2):
            small=word1
        else:
            small=word2
        merged = ''
        for i in range(len(small)):
            merged+=word1[i]
            merged+=word2[i]
        if small==word1:
            merged+=word2[i+1:]
        else:
            merged+=word1[i+1:]
        return merged