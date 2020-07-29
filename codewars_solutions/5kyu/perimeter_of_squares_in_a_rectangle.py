# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3,
# 5, 8. It's easy to see that the sum of the perimeters of these squares is : 
# 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80

# Could you give the sum of the perimeters of all the squares in a rectangle
# when there are n + 1 squares disposed in the same manner as in the drawing:

# ( Image found here: https://i.imgur.com/EYcuB1wm.jpg )

# Hint: See Fibonacci sequence #Ref: http://oeis.org/A000045

# The function perimeter has for parameter n where n + 1 is the number of 
# squares (they are numbered from 0 to n) and returns the total perimeter of 
# all the squares.

def perimeter(n):
    prev_num = 0
    curr_num = 1
    total_length = 1

    for i in range(n):
        prev_num, curr_num = curr_num, prev_num + curr_num
        total_length += curr_num

    return total_length * 4