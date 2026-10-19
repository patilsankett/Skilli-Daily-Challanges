#1 Largest Odd Number in a string
def largestOddNumber(s: str) :
    for i in range(len(s)-1,-1,-1):
        if int(s[i]) % 2==1:
            return int (s[:i+1])
    return ""

#2 Longest Common Prefix
def longestCommonPrefix(str: list[str]) -> str:
    if not str:
        return ""
    lo, hi = min(str), max(str)
    for i, ch in enumerate(lo):
        if ch != hi[i]:
            return lo[:i]
    return lo

#3 Isomorphic Strings
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for a, b in zip(s, t):
        if a in s_to_t and s_to_t[a] != b:
            return False
        if b in t_to_s and t_to_s[b] != a:
            return False
        s_to_t[a] = b
        t_to_s[b] = a

    return True
