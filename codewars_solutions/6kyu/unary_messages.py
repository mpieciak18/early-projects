# Binary with 0 and 1 is good, but binary with only 0 is even better!
# Originally, this is a concept designed by Chuck Norris to send so called
# unary messages.

# Can you write a program that can send and receive this messages?

# Rules:
# - The input message consists of ASCII characters between 32 and 127 (7-bit).
# - The encoded output message consists of blocks of 0.
# - A block is separated from another block by a space.
# - Two consecutive blocks are used to produce a series of same value bits 
# (only 1 or 0 values).
# - First block is always 0 or 00. If it is 0, then the series contains 1, 
# if not, it contains 0.
# - The number of 0 in the second block is the number of bits in the series.

# Example:
# Let’s take a simple example with a message which consists of only one
# character (Letter 'C'). 'C' in binary is represented as 1000011, so with 
# Chuck Norris’ technique this gives:

# 0 0 - the first series consists of only a single 1
# 00 0000 - the second series consists of four 0
# 0 00 - the third consists of two 1

# So 'C' is coded as: 0 0 00 0000 0 00

# Second example, we want to encode the message "CC"
# (i.e. the 14 bits 10000111000011):

# 0 0 - one single 1
# 00 0000 - four 0
# 0 000 - three 1
# 00 0000 - four 0
# 0 00 - two 1

# So "CC" is coded as: 0 0 00 0000 0 000 00 0000 0 00

def send(s):
    bin_string = ''
    
    for i in range(0, len(s)):
        integer = ord(s[i])
        val = bin(integer).replace('0b','')
        if len(val) == 6:
            val = '0' + val
        bin_string += val
    
    bin_vals = ''

    for i in range(0, len(bin_string)):
        if i == 0:
            bin_vals = bin_string[i]
        else:
            if bin_string[i] != bin_string[i-1]:
                bin_vals += ' ' + bin_string[i]
            else:
                bin_vals += bin_string[i]

    bin_vals = bin_vals.split(' ')
    digit_list = []

    for val in bin_vals:
        if int(val) == 0:
            digit_list.append('00')
        else:
            digit_list.append('0')
        digit_list.append(len(val) * '0')
    
    unary_string = ' '.join(digit_list)
    return unary_string

def receive(s):
    digit_list = [x for x in s.split(" ")]
    which_digit = [str(x) for x in digit_list[::2]]

    for i in range(0, len(which_digit)):
        if which_digit[i] == '0':
            which_digit[i] = 1
        else:
            which_digit[i] = 0
            
    digit_count = [x for x in digit_list[1::2]]

    for i in range(0, len(digit_count)):
        count = len(str(digit_count[i]))
        digit_count[i] = count
        
    bin_vals = ''

    for i in range(0, len(which_digit)):
        bin_vals += (str(which_digit[i]) * int(digit_count[i]))
    
    count = 0

    for i in range(0, len(bin_vals)):
        if i == 0:
            bin_vals = '0' + bin_vals
            count = 1
        elif i % 7 == 0:
            bin_vals = bin_vals[0:(i+count)] + '0' + bin_vals[(i+count):]
            count += 1
    
    ascii_string = ''

    for i in range(0, len(bin_vals), 8):
        val = bin_vals[i:(i+8)]
        integer = int(val, 2)
        character = chr(integer)
        ascii_string += character

    return ascii_string