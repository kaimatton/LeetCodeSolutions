# BRUTE FORCE METHOD. 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        n = len(nums)                               # sets n as the length of the lists nums 
        for i in range(n-1):                        # sets the index for each element in list of nums. now the len starts at index 0 instead of 1. 
            for j in range(i + 1, n):               # add one to the indices for as long as i is less than n 
                if nums[i] + nums[j] == target:     # finds the indices that finally add up to the target 
                    return [i,j]                    # returns the indices of the integer on list
        return []                                   # returns nothing if there is no solution
