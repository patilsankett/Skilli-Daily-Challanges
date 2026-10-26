def isArmstrong(n):
    d = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp%10
        total += digit**d
        temp //= 10
    return total == n