import math

def sqrt( integer: int)->int :
 
    if integer < 0:
        Error='Please enter a positive integer'
        return Error
    if integer == 1 :
        return integer
    if integer == 0:
        return integer
    if integer is None:
        return None


    first_integer = 1
    second_integer = integer

    while  first_integer <= second_integer :
        midpoint = ( first_integer + second_integer) // 2
        square_of_midpoint = midpoint * midpoint
        
        if square_of_midpoint == integer:
            return midpoint
        
        if square_of_midpoint > integer:
            second_integer=midpoint-1            
        else:
            first_integer = midpoint + 1
            answer = midpoint
    return answer


# Test cases 
# Test case 1
print("Pass" if  (3 == sqrt(9)) else "Fail")
# Test case 2
print("Pass" if  (4 == sqrt(16)) else "Fail")
# Test case 3
print("Pass" if  (1 == sqrt(1)) else "Fail")
# Test case 4
print("Pass" if  (5 == sqrt(27)) else "Fail")
# Edge case 1
print("Pass" if  ('Please enter a positive integer' == sqrt(-1)) else "Fail")
# Edge case 2
print("Pass" if  (0 == sqrt(0)) else "Fail")