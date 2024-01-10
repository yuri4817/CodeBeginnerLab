"""
The function notDivisibleNumbers(x, y) finds numbers between 1 and x that leave a remainder when divided by y, and returns them as a string separated by "-". 
For example, with x = 10 and y = 3, the numbers 1, 2, 4, 5, 7, 8, 10 leave a remainder when divided by 3, so it returns the string "1-2-4-5-7-8-10".
However, if x = 1 and y = 1, since 1 is the only divisor of 1, there are no numbers that leave a remainder, and thus nothing to return as a string, so the function is not defined. 
Additionally, this function does not work correctly if x or y are negative numbers or decimals.
"""

def notDivisibleNumbers(x,y):
    string = ""

    for i in range(1,x+1):
        if i % y != 0:
            string += str(i) + "-" 

    return string[:-1]



