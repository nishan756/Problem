def diagonalDifference(arr):
    # Write your code here
    
    _right = 0
    _left = 0
    right_index = 0
    left_index = len(arr) - 1
    for array in arr:
        _right += array[right_index]
        _left += array[left_index]
        
        right_index += 1
        left_index -= 1
    
    return abs((_left - _right))