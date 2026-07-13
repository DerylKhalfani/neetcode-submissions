class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        counter = {}

        for i in nums:

            count = counter.get(i, 0) + 1

            counter[i] = count

            if counter[i] > 1:
                print(counter)
                return True
        
        print(counter)
        return False