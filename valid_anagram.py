# Valid Anagram
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 &lt;= len(s), len(t) &lt;= 5 * 10^4
# s and t consist of lowercase English letters.
# Examples
# Example 1:
# Input: {"s": "anagram", "t": "nagaram"}
# Output: true
# Explanation: Sample testcase example
# Example 2:
# Input: {"s": "rat", "t": "car"}
# Output: false
# Explanation: Sample testcase example
# Example 3:
# Input: {"s": "a", "t": "a"}
# Output: true
# Explanation: Sample testcase example

# def isAnagram(s: str, t: str) -> bool:
#     # Write your solution here
#     if len(s) != len(t):
#         return False
#     count = [0] * 26
#     for a , b in zip (s,t):
#         count[ord(a)- ord ('a')] += 1
#         count[ord(b)- ord ('a')] -=1
#     return all(c == 0 for c in count)

def anagram(n1,n2):
    freq = [0]*10

    while (n1!= 0):
        last_digit = n1%10
        freq[last_digit] +=1
        n1 //= 10

    while (n2 != 0):
        last_digit = n2%10
        freq[last_digit] -=1
        n2 //= 10

    for i in freq:
        if (i != 0):
            return False
    return True

n1=1221
n2=1212

res=anagram(n1,n2)
print(f"{n1} and {n2} are anagram : {res}")