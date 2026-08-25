class Solution:
    def validPalindrome(self, s: str) -> bool:
        pointer1, pointer2 = 0, len(s) - 1

        def helper(substring: str):
            l, r = 0, len(substring) - 1

            while l < r:
                if substring[l] == substring[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        while pointer1 < pointer2:
            
            if s[pointer1] == s[pointer2]:
                pointer1 += 1
                pointer2 -= 1
        
            if s[pointer1] != s[pointer2]:
                    return helper(s[pointer1 + 1:pointer2+1]) or helper(s[pointer1:pointer2])

        return True





        