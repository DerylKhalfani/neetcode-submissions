class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        string = ""
        pointer = -1

        for i in range(min(len(word1), len(word2))):
            pointer = i

            string += word1[i]

            string += word2[pointer]
        
        string += word1[len(word2):]
        string += word2[len(word1):]

        return string

        