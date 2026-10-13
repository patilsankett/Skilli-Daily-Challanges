#1 Digit in a Number
class Solution:
    def digitCounts(self, n: int) -> int:
        return len(str(abs(n)))

#2 Count Odd Digits
def countOddDigits(n):
    count = 0
    while n>0:
        if (n % 10) % 2 == 1:
            count += 1
        n //=10
    return count

#3 Reverse an Integer
def reverseInteger(n):
    sign = -1 if n<0 else 1
    n = abs(n)
    rev = 0
    while n > 0:
        rev = rev*10+n%10
        n //= 10
    return sign * rev

#4 Palindrome Number
def isPalindrome(n):
    original = n
    rev = 0
    while n > 0:
        rev = rev*10 + n%10
        n//=10
    return original == rev

#5 Return the Largest Digit in a Number
def returnLargestDigit(n):
    return int(max(str(n)))

#6 Factorial of a Given Number
def factorial(n):
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

#7 Check if the Number is Armstrong
def isArmstrong(n):
    d = len(str(n))
    total = 0
    temp = n
    while temp > 0:
        digit = temp%10
        total += digit**d
        temp //= 10
    return total == n
