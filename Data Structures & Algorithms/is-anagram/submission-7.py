class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        hashmap_s = {}
        hashmap_t = {}

        for i in range(len(s)):
            count_s = hashmap_s.get(s[i], 0) + 1
            count_t = hashmap_t.get(t[i], 0) + 1

            hashmap_s[s[i]] = count_s
            hashmap_t[t[i]] = count_t
        
        return hashmap_s == hashmap_t