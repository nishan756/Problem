class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        element_status = dict()
    
        for i in nums:
            if i not in element_status:
                element_status[i] = False
        

        longest_length = 0
        
        for i in nums:
            currentLength = 1
            
            next_num = i + 1
            while next_num in element_status and element_status[next_num] == False:
                currentLength += 1
                element_status[next_num] = True
                next_num += 1
            
            prev_num = i - 1
            while prev_num in element_status and element_status[prev_num] == False:
                currentLength += 1
                element_status[prev_num] = True
                prev_num -= 1
            
            element_status[i] = True
            longest_length = max(longest_length , currentLength)
                
        return longest_length
      
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) 
    
        longest = 0
        
        for num in num_set:
            
            if num - 1 not in num_set:
                length = 1
                current = num
                
                while current+1 in num_set:
                    length += 1
                    current += 1
                    
                longest = max(longest , length)
        
        return longest

  
