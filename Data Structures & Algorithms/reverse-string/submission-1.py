class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        for i in range(0, len(s) // 2, 1):
            temp1 = s[-i - 1]
            temp2 = s[i]
            s[-i - 1] = temp2
            s[i] = temp1

            print(i)

        