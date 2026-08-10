class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(s.split())
        l,r = 0, len(s) - 1
        
        while l < r:

            while not s[r].isalpha() and not s[r].isdigit():
                r -= 1
                if r < l:
                    return True

            while not s[l].isalpha() and not s[l].isdigit():
                l += 1
                if l > r:
                    return True

            print(s[l].lower(), s[r].lower())
            print(l, r)
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
                continue
            
            if l > r:
                return True
            else:
                return False
        
        return True