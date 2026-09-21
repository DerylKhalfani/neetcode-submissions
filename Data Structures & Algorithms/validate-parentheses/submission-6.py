class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {'}': '{', ']': '[', ')': '('}

        key_list = ['}', ']', ')']

        stack = []


        for char in s:
            print(stack, 'stack')
            print(char, 'char')
            if char in key_list:

                if len(stack) == 0:
                    return False
                
                # print(char)
                hashmap_char = hashmap.get(char)
                stack_char = stack.pop()

                print(hashmap_char, 'hashmap_char')
                print(stack_char, 'stack_char')

                if hashmap_char != stack_char:
                    return False

            else:
                stack.append(char)

        if len(stack) == 0:
            return True
        else:
            return False
        