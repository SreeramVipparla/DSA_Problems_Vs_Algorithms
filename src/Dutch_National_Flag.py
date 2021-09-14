def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    start = 0
    end = len(input_list) - 1

    initial_idx = 0

    while initial_idx <= end :
        if input_list[initial_idx] == 2:
            input_list[end] = 2
            input_list[initial_idx] = input_list[end]
            end -= 1
       
        elif input_list[initial_idx] is 0:
            input_list[initial_idx] = input_list[start]
            start += 1
            initial_idx += 1
        else:
            initial_idx += 1

    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")
# Test cases

# Test case 1
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
# Expected output
# [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass

# Test case 2
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
# Expected output
# [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
# Pass

# Test case 3
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
# Expected output
# [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
# Pass

# Edge case 1
test_function([])
# Expected output
# []
# Pass

# Edge case 2
test_function([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
# Expected output
# [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# Pass


