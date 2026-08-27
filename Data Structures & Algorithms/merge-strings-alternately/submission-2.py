class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        string = ""

        for i in range(min(len(word1), len(word2))):
            pointer = i

            string += word1[i]

            string += word2[pointer]
        
        if len(word1) > len(word2):
            string += word1[pointer + 1:]

        elif len(word2) > len(word1):
            string += word2[pointer + 1:]

        return string

        