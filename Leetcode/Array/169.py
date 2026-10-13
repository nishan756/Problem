"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
The input is generated such that a majority element will exist in the array.

"""
from typing import List

class Solution:
    # Solution - 01
    def sol1(self , nums:List[int])->int:
        num = None
        count = 0
        for i in range(len(nums)):
            num =  nums[i]
            for i in range(len(nums)):
                if nums[i] == num:
                    count += 1
            
            if count > int((len(nums))/2):
                return num
        else:
            return -1
    
    # Solution - 02
    def sol2(self , nums:List[int])->None:
        freq_dict = {}
        for i in nums:
            if i in freq_dict:
                freq_dict[i] += 1
            else:
                freq_dict[i] = 1
        
        for j in freq_dict:
            if freq_dict[j] > len(nums) // 2:
                return j
        return -1
    
    # Solution - 03 (Moore's voting algorithm)
    def sol3(self , nums:List[int])->int:
        item = None
        count = 0
        for i in nums:
            if count == 0:
                item = i
            if item == i:
                count += 1
            else:
                count -= 1
        return item


s = Solution()
print("Solution - 1")
print(s.sol1([3,2,3]))
print(s.sol1([2,2,1,1,1,2,2]))
print(s.sol1([1]))
print(s.sol1([5,5,5,2,3,5,4]))
print(s.sol1([-1,-1,-1,2,3]))
print(s.sol1([0,0,0,1,2,0,3]))

print("Solution - 2")
print(s.sol2([3,2,3]))
print(s.sol2([2,2,1,1,1,2,2]))
print(s.sol2([1]))
print(s.sol2([5,5,5,2,3,5,4]))
print(s.sol2([-1,-1,-1,2,3]))
print(s.sol2([0,0,0,1,2,0,3]))

print("Solution - 3")
print(s.sol3([3,2,3]))
print(s.sol3([2,2,1,1,1,2,2]))
print(s.sol3([1]))
print(s.sol3([5,5,5,2,3,5,4]))
print(s.sol3([-1,-1,-1,2,3]))
print(s.sol3([0,0,0,1,2,0,3]))