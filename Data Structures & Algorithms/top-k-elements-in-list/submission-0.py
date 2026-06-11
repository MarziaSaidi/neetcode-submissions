class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        # Count frequencies
        for item in nums:
            if item in hashmap:
                hashmap[item] += 1
            else:
                hashmap[item] = 1

        # Sort by frequency (descending) and return top k keys
        return sorted(hashmap, key=lambda x: hashmap[x], reverse=True)[:k]