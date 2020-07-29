# Create a function that transforms any positive number to a string representing
# the number in words. The function should work for all numbers between 0 and 
# 999999.

# Examples:

# number2words(0)  ==>  "zero"
# number2words(1)  ==>  "one"
# number2words(9)  ==>  "nine"
# number2words(10)  ==>  "ten"
# number2words(17)  ==>  "seventeen"
# number2words(20)  ==>  "twenty"
# number2words(21)  ==>  "twenty-one"
# number2words(45)  ==>  "forty-five"
# number2words(80)  ==>  "eighty"
# number2words(99)  ==>  "ninety-nine"
# number2words(100)  ==>  "one hundred"
# number2words(301)  ==>  "three hundred one"
# number2words(799)  ==>  "seven hundred ninety-nine"
# number2words(800)  ==>  "eight hundred"
# number2words(950)  ==>  "nine hundred fifty"
# number2words(1000)  ==>  "one thousand"
# number2words(1002)  ==>  "one thousand two"
# number2words(3051)  ==>  "three thousand fifty-one"
# number2words(7200)  ==>  "seven thousand two hundred"
# number2words(7219)  ==>  "seven thousand two hundred nineteen"
# number2words(8330)  ==>  "eight thousand three hundred thirty"
# number2words(99999)  ==>  "ninety-nine thousand nine hundred ninety-nine"
# number2words(888888)  ==>  "eight hundred eighty-eight thousand eight hundred
# 							  eighty-eight"

def number2words(n):
    dict_one = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
        5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
        10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
    dict_two = {2: "twenty", 3: "thirty", 4: "forty", 5: "fifty",
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"}
    answer = ''
    num = str(n)  
    
    for i in reversed(range(0, len(num))):
        if i == 5:
            if int(num[-i-1]) != 0:
                answer += dict_one[int(num[-i-1])]
                answer += " hundred"
                if int(num[-i] + num[-i+1]) != 0:
                    answer += " "
        elif i == 4:
            if int(num[-i-1] + num[-i]) >= 20:
                answer += dict_two[int(num[-1-i])]
            if int(num[-i-1] + num[-i]) >= 20 and int(num[-i]) != 0:
                answer += "-"
            elif int(num[-i-1] + num[-i]) < 20 and int(num[-i-1] + num[-i]) >= 10:   
                answer += dict_one[int(num[-i-1] + num[-i])]
        elif i == 3:
            if answer != '':
                if int(num[-i-1]) != 0:
                    if int(num[-i-2] + num[-i-1]) >= 20 or int(num[-i-2] + num[-i-1]) < 10:
                        answer += dict_one[int(num[-i-1])]
            else:
                answer += dict_one[int(num[-i-1])]
            answer += " thousand"
            if int(num[-i:]) != 0:
                answer += " "
        elif i == 2:
            if int(num[-i-1]) != 0:
                answer += dict_one[int(num[-i-1])]
                answer += " hundred"
                if int(num[-i] + num[-i+1]) != 0:
                    answer += " "
        elif i == 1:
            if int(num[-i-1] + num[-i]) >= 20:
                answer += dict_two[int(num[-1-i])]
            if int(num[-i-1] + num[-i]) >= 20 and int(num[-i]) != 0:
                answer += "-"
            elif int(num[-i-1] + num[-i]) < 20 and int(num[-i-1] + num[-i]) >= 10:   
                answer += dict_one[int(num[-i-1] + num[-i])]
        elif i == 0:
            if answer != '':
                if int(num[-i-1]) != 0:
                    if int(num[-i-2] + num[-i-1]) >= 20 or int(num[-i-2] + num[-i-1]) < 10:
                        answer += dict_one[int(num[-i-1])]
            else:
                answer += dict_one[int(num[-i-1])]

    return answer