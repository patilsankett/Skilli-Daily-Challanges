#1 Check for Perfect Number
def isPerfectNumber(n):
    if n <= 1:
        return False
    total = 1
    i = 2
    while i*i <= n:
        if n%i ==0:
            total += i
            if  i != n // i:
                total += n//i
        i +=1
    return total == n

#2 Check for Prime Number
def isPrime(n):
    if n < 2:
        return False
    i=2
    while i*i <=n:
        if n%i ==0:
            return False
        i +=1
    return True

#3 Count of Prime Numbers till N
def countPrimes(n):
    count = 0
    for num in range (2,n+1):
        i=2
        while i*i <=num:
            if num %i ==0:
                break
            i += 1
        else:
            count+= 1 
    return count

#4 GCD of Two Numbers
def gcdOfTwoNumbers(n1, n2):
    while n2 != 0:
        n1, n2 =n2, n1 %n2
    return n1

#5 Lowest Common Multiple (LCM) of Two Numbers
def findLcm(n1, n2):
    a,b = n1,n2
    while b!=0:
        a,b = b,a%b
    return n1 // a *n2

#6 Find Divisors of a Number
def findDivisors(n):
    result = []
    i=1
    while i*i <= n:
        if n%i ==0:
            result.append(i)
            if i != n// i:
                result.append(n//i)
        i +=1
    result.sort()
    return result