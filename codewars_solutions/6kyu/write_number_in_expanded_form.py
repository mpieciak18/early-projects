# Write Number in Expanded Form

# You will be given a number and you will need to return it as a string
# in Expanded Form. For example:

# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'

# NOTE: All numbers will be whole numbers greater than 0.

def expanded_form(num):
    # Convert int to list of int values.
    num_list = [int(i) for i in str(num)]
    
    # Transform non-zero values to include appropriate amount of zeroes.
    for x in range(0, len(num_list)):
        if num_list[x] != 0:
            num_list[x] = (10**(len(num_list[x:]) - 1)) * num_list[x]
            
    expanded_list = ''
    
    # Take new non-zero values from list and create string.
    for i in num_list:
        if i == num_list[0]:
            expanded_list = f"{i}"
        elif i != 0:
            expanded_list = f"{expanded_list} + {i}"
            
    return expanded_list