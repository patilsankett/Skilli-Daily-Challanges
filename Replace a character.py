class Solution:
    def replaceCharacter(self, s, oldChar, newChar):
        # Write your logic here

        result = []
        for ch in s:
            if ch == oldChar:
                result.append(newChar)
            else:
                result.append(ch)
        return "".join(result)