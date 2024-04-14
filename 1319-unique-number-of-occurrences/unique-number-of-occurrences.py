class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        val_freq = dict()
        for num in arr:
            if num in val_freq:
                val_freq[num] += 1
            else:
                val_freq[num] = 1
        if len(set(val_freq.values())) < len(val_freq.values()):
            return False
        else:
            return True