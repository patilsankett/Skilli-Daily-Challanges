#Largest Odd Number in a string
def largestOddNumber(s: str) :
    for i in range(len(s)-1,-1,-1):
        if int(s[i]) % 2==1:
            return int (s[:i+1])
    return ""