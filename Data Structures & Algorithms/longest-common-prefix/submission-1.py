class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        hashmap = {}
        string = ""

        min_len = min(len(word) for word in strs)
        
        for i in range(min_len):
            for word in strs:
                count = hashmap.get(word[i], 0) + 1
                hashmap[word[i]] = count

            print(hashmap)
            char, value = list(hashmap.items())[0]

            if value == len(strs):
                string += char
            else:
                return string
            
            hashmap = {} 

        return string