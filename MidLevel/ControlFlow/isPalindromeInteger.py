def isPalindromeInteger(n):
    
    str_n = str(n)
    reverse_str_n = str_n[::-1]
    return str_n == reverse_str_n
