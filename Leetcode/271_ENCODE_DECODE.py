from typing import List
class Codec:
    
    def __init__(self , strs:List):
        self.strs = strs
        
    def encode(self):
        encoded = ""
        for s in self.strs:
            encoded += str(len(s)) + "#" + s
        
        return encoded
    
    def decode(self , string):
        result = []
        
        i = 0
        while i < len(string):
            j = i
            
            while string[j] != "#":
                j += 1
            
            length = int(string[i:j])
            
            word = string[j+1:j+1+length]
            
            result.append(word)
        
            i += j+1+length 
        
        return result
    
codec = Codec(["django" , "django rest framework"])
print(codec.encode())
print(codec.decode(codec.encode()))
