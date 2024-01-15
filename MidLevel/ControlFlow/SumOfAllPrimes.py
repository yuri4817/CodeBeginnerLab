def isPrime(number):
    for i in range(2, number) :
        if number % i == 0: return False
    
    return number > 1


def sumOfAllPrimes(n):
    primNum = 0
    
    for i in range(2, n+1):
        if isPrime(i):
            primNum += i
            

    return primNum






