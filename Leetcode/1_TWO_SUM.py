#Better solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            extra = target-nums[i]
            if extra in hashMap:
                return [i , hashMap[extra]]
            else:
                hashMap[nums[i]] = i
        return False
                
       