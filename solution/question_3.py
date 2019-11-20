class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        max = 0
        start = 0
        if len(s) == 0 or s is None:
            return max
        for i in range(len(s)):
            if hash_map.get(s[i]) is not None:
                if start < hash_map[s[i]]:
                    start = hash_map[s[i]]
            if i - start + 1 > max:
                max = i - start + 1
            hash_map[s[i]] = i + 1
        return max
