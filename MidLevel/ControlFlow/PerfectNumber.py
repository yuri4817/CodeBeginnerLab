"""
Define a function perfectNumberList which returns a string listing all perfect numbers within the range from 2 to a given natural number n, 
separated by '-'. A perfect number is a natural number that is equal to the sum of its divisors, 
excluding itself. If there are no perfect numbers, return the string 'none'.
"""

def perfectNumberList(n):
    output = ""
    if n < 6:
        return "none"
    for num in range(2, n + 1):
        divisors = 0
        for i in range(1, num):
            if num % i == 0:
                divisors += i 
        if divisors == num:
            output += str(num) + "-"
    
    return output[:-1]


"""
I have written the code above, but it is processing heavy, so I will describe a more lightweight version of the code below.
"""
import math
def perfectNumberList(n):
    numbers = ''
    for i in range(2, n+1) :
        if isPerfect(i): numbers += str(i) + '-'
    
    return numbers[0:-1] if numbers != '' else 'none'


def isPerfect(x) :
    divisors = 1
    n = math.ceil(math.sqrt(x))
    for i in range(2, n) :
        if x % i == 0:
            divisors += i
            divisors += x / i
    return x == int(divisors)
