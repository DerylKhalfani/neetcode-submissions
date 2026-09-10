class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first_pointer = len(nums1) - len(nums2) - 1
        second_pointer = len(nums1) - 1
        third_pointer = len(nums2) - 1


        i = 0

        while first_pointer >= 0 and third_pointer >= 0:
            
            print(f'epoch {i}')
            print('first_pointer', first_pointer)
            print(nums1[first_pointer])
            print('second_pointer', second_pointer)
            print(nums1[second_pointer])
            print('third_pointer', third_pointer)
            print(nums2[third_pointer])
            print(nums1)

            if nums1[first_pointer] > nums2[third_pointer]:
                nums1[second_pointer] = nums1[first_pointer]
                
                first_pointer -= 1
                
                second_pointer -= 1

            else:
                nums1[second_pointer] = nums2[third_pointer]

                third_pointer -= 1
                
                second_pointer -= 1

        while third_pointer >= 0:
            print('second while loop')
            print(second_pointer)
            print(third_pointer)
            nums1[second_pointer] = nums2[third_pointer]

            third_pointer -= 1
            second_pointer -= 1
            
            
        
            




