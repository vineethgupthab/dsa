class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map = dict()
        num_of_operation = 0
        for i in nums:
            if i in hash_map and hash_map[i] > 0:
                hash_map[i] -= 1
                num_of_operation += 1
            else:
                hash_map[k-i] = hash_map.get(k-i, 0) + 1
        return num_of_operation