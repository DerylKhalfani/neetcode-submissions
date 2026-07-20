class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        dummy = nums.copy()
        for i in dummy:
            print(i)
            if i == val:
                nums.remove(i)
                print(nums)
        
        return len(nums)
        