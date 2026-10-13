def gcdOfTwoNumbers(n1, n2):
    # Write your code here
    while n2 != 0:
        n1, n2 =n2, n1 %n2
    return n1