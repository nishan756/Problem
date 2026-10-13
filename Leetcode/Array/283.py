"""
MOVES ZERO 
-----------

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""
from typing import List

class Solution:
    # Solution - 01
    def sol1(self , nums:List[int])->None:
        zero_array = []
        non_zero_array = []
        for i in nums:
            if i == 0:
                zero_array.append(0)
            else:
                non_zero_array.append(i)
        final_array = non_zero_array + zero_array
        print(final_array)

    # Solution - 02
    def sol2(self , nums:List[int])->None:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.append(0)
                nums.pop(i)
        print(nums)
    
    # Solution - 03
    def sol3(self , nums:List[int])->None:
        z_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[z_index] , nums[i] = nums[i] , nums[z_index]
                z_index += 1
        print(nums)

s = Solution()
s.sol1([0 , 1 , 0 , 2 , 5 , 6 , 7 , 0])
s.sol2([0 , 1 , 0 , 2 , 5 , 6 , 7 , 0])
s.sol3([0 , 1 , 0 , 2 , 5 , 6 , 7 , 0])


