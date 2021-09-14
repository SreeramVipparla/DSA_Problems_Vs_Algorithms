def rotated_array_search(input_list, integer_in_array):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end= len(input_list) - 1
    while start <= end:
        midpoint_of_array = (start+end) // 2
        if integer_in_array== input_list[midpoint_of_array]:
            return midpoint_of_array

        if input_list[start] <= input_list[midpoint_of_array]:
            if input_list[start] <= integer_in_array <= input_list[midpoint_of_array]:
                end = midpoint_of_array - 1

            else:
                start = midpoint_of_array + 1
        else:

            if not input_list[midpoint_of_array] <=integer_in_array and  integer_in_array <= input_list[end]:
                start = midpoint_of_array + 1

            else:
                end = midpoint_of_array - 1
    return -1
    

def linear_search(input_list, integer_in_array):
    for index, element in enumerate(input_list):
        if element == integer_in_array:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    integer_in_array = test_case[1]
    if linear_search(input_list, integer_in_array) == rotated_array_search(input_list, integer_in_array):
        print("Pass")
    else:
        print("Fail")
# Test cases
# Test case 1
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# Test case 2
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# Test case 3
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
# Edge cases
# Edge case 1
test_function([[], 10])
# Edge case 2
test_function([[], []])
# Edge case 3
test_function([[], -1])