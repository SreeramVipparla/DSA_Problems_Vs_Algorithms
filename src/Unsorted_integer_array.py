def get_min_max(integers):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(integers) == 0:
        return None


    lower_bound_value = 1000   
    upper_bound_value = 0
    
    
    for test_case in integers:
        if test_case < lower_bound_value:
            lower_bound_value = test_case
        if test_case > upper_bound_value:
            upper_bound_value = test_case
    return (lower_bound_value, upper_bound_value)

import random
l = [i for i in range(0, 10)] 
random.shuffle(l)
# Test case 1
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
# Test case 2
print ("Pass" if ((53, 143) == get_min_max([65,76,87,143,53])) else "Fail")
# Edge Case
print ("Pass" if (None == get_min_max([])) else "Fail")