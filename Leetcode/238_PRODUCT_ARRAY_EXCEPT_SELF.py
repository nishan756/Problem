class productExceptSelf:
    
    def __init__(self , array:list):
        self.array = array
    
    def solution1(self):
        multiply = 1
        
        for i in self.array:
            multiply *= i
        
        result = []
        
        for i in self.array:
            result.append(multiply // i)
        
        return result #This is not valid. Cz leetcode restrict not to use division operator
    
    def solution2(self):
        length = len(self.array)
    
        left = [1] * length
        right = [1] * length
        result = [1] * length
    
        for i in range(1, length):
            left[i] = self.array[i - 1] * left[i - 1]
    
        for i in range(length - 2, -1, -1):
            right[i] = self.array[i + 1] * right[i + 1]
    
        for i in range(length):
            result[i] = left[i] * right[i]
    
        return result
        
        
    
obj1 = productExceptSelf([1 , 2 , 3 , 4])
print(obj1.solution1())
print(obj1.solution2())
