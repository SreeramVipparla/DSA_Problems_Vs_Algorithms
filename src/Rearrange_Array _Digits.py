def mergesort(initial, final):
            initial_count = 0
            final_count = 0
            expected_outcome = []
            while initial_count < len(initial) and final_count < len(final):
                if initial[initial_count] > final[final_count]:
                    expected_outcome.append(final[final_count])
                    final_count += 1
                else:
                    expected_outcome.append(initial[initial_count])
                    initial_count += 1
            expected_outcome.extend(final[final_count:])
            expected_outcome.extend(initial[initial_count:])
            

            return expected_outcome

def sort(list_of_ints):
            while len(list_of_ints) <= 1:
                return list_of_ints

            midpoint_of_ints = int(len(list_of_ints) / 2)
            initial = sort(list_of_ints[:midpoint_of_ints])
            final=sort(list_of_ints[midpoint_of_ints:])
            return mergesort(initial, final)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two list_of_nums_ber such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = sort(input_list)

    list_of_nums__1 = 0
    list_of_nums__2 = 0
    length=len(input_list)
    for i in range(length - length // 2):
       list_of_nums__2 += sorted_list[(2*i)] * (10**i)
    for i in range(length// 2):
       list_of_nums__1 += sorted_list[(2*i+1)] * (10**i)
    
    return list_of_nums__1, list_of_nums__2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# Test cases

# Test case 1
test_function([[1, 2, 3, 4, 5], [542, 31]])
# Test case 2 
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
# Edge case 1
test_function([[],[]])
# Edge case 2 
test_function([[3, 4], [3, 4]])
# Edge case 3
test_function([[-1],[-1]])