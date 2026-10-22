from collections import Counter

def anagram(n1: int, n2: int) -> bool:
    return Counter (str(n1)) == Counter(str(n2))