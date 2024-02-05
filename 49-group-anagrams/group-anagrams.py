class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comb = dict(); sets = []; vals = []
        for word in strs:
            if sorted(word) not in sets:
                comb[word] = [word]
                sets.append(sorted(word))
                vals.append(word)
            else:
                comb[vals[sets.index(sorted(word))]].append(word)
        return [sorted(vals) for vals in comb.values()]