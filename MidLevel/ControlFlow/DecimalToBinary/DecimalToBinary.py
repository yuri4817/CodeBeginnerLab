def decimalToBinary(decNumber):
    binary = ""
    while decNumber > 0:
        remainder = decNumber % 2
        binary = str(remainder) + binary
        decNumber //= 2
    return binary
