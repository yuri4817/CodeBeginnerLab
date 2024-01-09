
"""
In R University, if a student misses more than 3 classes in any course, they cannot earn credits for that course. 
Create a function named doYouFail that returns "pass" if earning credits is possible and "fail" if not, based on the given string string composed of P for Participate and A for Absence.
"""

def doYouFail(string):
    num = 0
    f = "fail"
    p = "pass"

    for i in range(len(string)):
        if string[i] == 'A':
            num += 1 

    if num >= 3:
        return f
    else:
        return p
