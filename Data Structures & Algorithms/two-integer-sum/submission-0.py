class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complement = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            index = complement.get(difference, None)

            if index != None:
                if index < i:
                    return [index, i]
                else:
                    return [i, index]
            
            complement[nums[i]] = i