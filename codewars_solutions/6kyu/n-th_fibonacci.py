# I love Fibonacci numbers in general, but I must admit I love some more than 
# others.

# I would like for you to write me a function that when given a number (n) 
# returns the n-th number in the Fibonacci Sequence.

# For example:

#    nth_fib(4) == 2

# Because 2 is the 4th number in the Fibonacci Sequence.

# For reference, the first two numbers in the Fibonacci sequence are 0 and 1,
# and each subsequent number is the sum of the previous two.

def nth_fib(n):
    # Set up variables for 3rd # of Fibonacci.
    second_last = 0
    last = 1
    answer = 1
    # Return answers for 1st, 2nd, & 3rd #s of Fibonacci.
    if n == 1:
        return second_last
    elif n == 2:
        return last
    elif n == 3:
        return answer
    # Solve for n'th # of Fibnoacci if n > 3.   
    else:
        new_last = None
        new_second_last = None
        for i in range(0, n-3):
            new_second_last = last
            new_last = answer
            answer = new_second_last + new_last
            last = new_last
            second_last = new_second_last
        return answer