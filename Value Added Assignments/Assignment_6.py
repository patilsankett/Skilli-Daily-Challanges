#1 Count Frequency of each Digit
def countFreq(n: int) -> list[int]:
    freq = [0] * 10
    for ch in str(n):
        freq[int(ch)] += 1
    return freq

#2 Count digits Appearing atleast K Times
def countFreq(n: int, k: int) -> list[int]:
    freq = [0]*10
    for ch in str(n):
        freq[int(ch)]+=1
    return [d for d in range(10)if freq[d]>=k]

#3 Check if two numbers are Anagram 
from collections import Counter
def anagram(n1: int, n2: int) -> bool:
    # Write your solution here
    return Counter(str(n1)) == Counter(str(n2))

