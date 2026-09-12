class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        first_pointer = 0
        second_pointer = 1

        while second_pointer < len(nums):

            if nums[first_pointer] != nums[second_pointer]:
                first_pointer += 1

                nums[first_pointer] = nums[second_pointer]

                second_pointer += 1
            
            elif nums[first_pointer] == nums[second_pointer]:
                second_pointer += 1

        return first_pointer + 1

        



        