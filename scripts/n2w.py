# Welcome to my first ever project!
# The following program takes a single integer as an argument, and returns it as
# as string of grammatically correct English words.
# The program consists of the following: 1. Dictionaries for the numbers/words.
# 2. Three helper functions, and 3. A master function, using #1 & #2.
# When reading the comments & trying to understand the program, I suggest you
# start with the master function, then work back up to the helper functions.
# Enjoy the program!

#### Dictionaries ####

# Dictionary consisting of num/word pairs for 0-19.
dict_one = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
    10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen"}
# Dictionary consisting of num/word pairs for 20, 30, 40, ..., 90.
dict_two = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
    6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
# Dictionary consisting of num/word pairs for "large numbers", ie "trillion".
dict_three = {1: "thousand", 2: "million", 3: "billion", 4: "trillion",
    5: "quadrillion", 6: "quintillion", 7: "sextillion", 8: "septillion",
    9: "octillion", 10: "nonillion", 11: "decillion", 12: "undecillion",
    13: "duodecillion", 14: "tredecillion", 15: "quattrodecillion",
    16: "quindecillion", 17: "sexdecillion", 18: "septendecillion",
    19: "octodecillion", 20: "novemdecillion", 21: "vigintillion"}

#### Helper Functions ####

# Helper function used for 0th, 3rd, 6th, etc. digits.
# Used if i % 3 == 0 in master function loop.
# Sets old_answer to answer, goes through rules to update answer (or not),
# checks to see if answer is updated, & returns updated answer or 'skip'.
def n2w_dig0(n,i,answer):
    # Sets old_answer to answer; checked for redundancy later.
    old_answer = answer
    # Continues if answer is NOT empty (means answer went through previous 
    # helper functions & current digit is not first digit of n).
    if answer != '':
        # Continues if current digit is NOT zero.
        if int(n[-i-1]) != 0:
            # Continues if last digit + current digit is greater than / equal 
            # to 20, or is less than 10.
            if int(n[-i-2] + n[-i-1]) >= 20 or int(n[-i-2] + n[-i-1]) < 10:
                # Appends answer with value from dict_one using current digit as 
                # dictionary key.
                answer += dict_one[int(n[-i-1])]
    # Continues if answer IS empty (means answer has NOT  gone through previous
    # helper functions & current digit IS first digit of n.)
    else:
        # Appends answer with value from dict_one using current digit as 
        # dictionary key. 
        answer += dict_one[int(n[-i-1])]
    # Continues if current digit is NOT last digit of n.
    if i != 0:
        # Continues if length of first digit to current digit of n is greater
        # than / equals 3.
        if len(n[:-i]) >= 3:
            # Continues if  2nd to last digit, last digit, and current digit
            # does NOT equal 0.
            if int(n[-i-3:-i]) != 0:
                # Appends answer with " " &  value from dict_three using [i/3]
                # as dictionary key. i/3 is used instead of i because dict_three
                # assigns 1, 2, 3, etc. (instead of 3, 6, 9, etc.) as keys to 
                # values thousand, million, billion, etc.
                answer += " " + dict_three[(i/3)]
                # Continues if current digit is NOT zero and appends answer with
                # " " for space between words.
                if int(n[-i:]) != 0:
                    answer += " "
        # Continues if length of first digit to current digit of n equals 2.
        elif len(n[:-i]) == 2:
            # Continues if last digit and current digit does NOT equal 0.
            if int(n[-i-2:-i]) != 0:
                # Appends answer with " " &  value from dict_three using [i/3]
                # as dictionary key. i/3 is used instead of i because dict_three
                # assigns 1, 2, 3, etc. (instead of 3, 6, 9, etc.) as keys to 
                # values thousand, million, billion, etc.
                answer += " " + dict_three[(i/3)]
                # Continues if current digit is NOT zero and appends answer with
                # " " for space between words.
                if int(n[-i:]) != 0:
                    answer += " "
        # ontinues if length of first digit to current digit of n equals 1.
        elif len(n[:-i]) == 1:
            # Continues if current digit does NOT equal 0.
            if int(n[-i-1:-i]) != 0:
                # Appends answer with " " &  value from dict_three using [i/3]
                # as dictionary key. i/3 is used instead of i because dict_three
                # assigns 1, 2, 3, etc. (instead of 3, 6, 9, etc.) as keys to 
                # values thousand, million, billion, etc.
                answer += " " + dict_three[(i/3)]
                # Continues if current digit is NOT zero and appends answer with
                # " " for space between words.
                if int(n[-i:]) != 0:
                    answer += " "
    # Continues if answer does NOT equal old_answer, and returns answer to 
    # master function loop. If answer equals old_answer, 'skip' is return to
    # master function loop.
    if answer != old_answer:
        return answer
    else:
        return 'skip'

# Helper function used for 1st, 4th, 7th, etc. digits.
# Used if i % 3 == 2 in master function.
# Sets old_answer to answer, goes through rules to update answer (or not),
# checks to see if answer is updated, & returns updated answer or 'skip'.
def n2w_dig1(n,i,answer):
    # Sets old_answer to answer; checked for redundancy later.
    old_answer = answer
    # Continues if current & last digits are greater than / equal 20 and appends
    # answer with value from dict_two using current digit as key.
    if int(n[-i-1] + n[-i]) >= 20:
        answer += dict_two[int(n[-i-1])]
    # Continues if current & last digits are greater than / equal 20 AND if 
    # current digit is NOT zero, and appends answer with hyphen.
    if int(n[-i-1] + n[-i]) >= 20 and int(n[-i]) != 0:
        answer += "-"
    # Continues if current & last digits are less than 20 AND greater than /
    # equal 10, and appends answer with value from dict_one using current &
    # last digits as key.
    elif int(n[-i-1] + n[-i]) < 20 and int(n[-i-1] + n[-i]) >= 10:   
        answer += dict_one[int(n[-i-1] + n[-i])]
    # Continues if answer does NOT equal old_answer, and returns answer to 
    # master function loop. If answer equals old_answer, 'skip' is return to
    # master function loop.
    if answer != old_answer:
        return answer
    else:
        return 'skip'

# Function used for 2nd, 5th, 8th, etc. digits.
# Used if i % 3 == 1 in master function.
def n2w_dig2(n,i,answer):
    # Sets old_answer to answer, goes through rules to update answer (or not),
    # checks to see if answer is updated, & returns updated answer or 'skip'.
    old_answer = answer
    # Continues if current digit does NOT equal zero, and appends answer with
    # value from dict_one using current digit as key AND with " hundred".
    if int(n[-i-1]) != 0:
        answer += dict_one[int(n[-i-1])]
        answer += " hundred"
        # Continues if current and next digits do NOT equal zero, and appends
        # answer with " " for space between words.
        if int(n[-i] + n[-i+1]) != 0:
            answer += " "
    # Continues if answer does NOT equal old_answer, and returns answer to 
    # master function loop. If answer equals old_answer, 'skip' is return to
    # master function loop.
    if answer != old_answer:
        return answer
    else:
        return 'skip'

#### Master Function ####

# Master function iterates through length of argument n and uses  3 helper
# functions to initiate and build string of grammatically correct words that
# represent integer N in plain English.
def num2words(n):
    # Continues if n is an integer, sets initial values for answer &
    # updated_answer, and converts n to integer.
	if isinstance(n, int) == True:
	    answer = ''
	    n = str(n)  
	    updated_answer = 'skip'
        # Iterates through values 0 to length of n - 1 & runs through helper
        # functions. Which helper function is determined by what position i is
        # in within 3.IE, digits in positions 0 & 3 trigger n2w_dig0, digits in
        # positions 1 & 4 trigger n2w_dig2, and etc. Answer variable updates 
        # each time if helper functions do not return 'skip.' Helper functions 
        # only returns 'skip' if the no change is deemed needed for a given
        # digit. Answer is return upon completion.
	    for i in reversed(range(0, len(n))):
	        if i % 3 == 0:
	            updated_answer = n2w_dig0(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer
	        if i % 3 == 1:
	            updated_answer = n2w_dig1(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer
	        if i % 3 == 2:
	            updated_answer = n2w_dig2(n,i,answer)
	            if updated_answer != 'skip':
	                answer = updated_answer    
	    return answer
    # Returns ValueError if argument n is not an integer.
	else:
		raise ValueError("Argument must be an integer.")