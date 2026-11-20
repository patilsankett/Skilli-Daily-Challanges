#Q1. Delete Element at given Index
from typing import List
def deleteAtIndex(arr: List[int], P: int) -> List[int]:
    return arr[:P] + arr[P + 1:] + [0]

#Q2. Delete all Ocurances of X
from typing import List
def deleteAllOccurrences(arr: List[int], X: int) -> List[int]:
    n = len(arr)
    result = [x for x in arr if x != X]
    result += [0] * (n - len(result))
    return result

#Q3. Insert Zero after Every Element
from typing import List
def insertZeroAfterEveryElement(arr: List[int]) -> List[int]:
    n = len(arr)
    expanded = []
    for x in arr:
        expanded.append(x)
        expanded.append(0)
    return expanded[:n]

#Q4. Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        pos = 0  # position to place the next non-zero element

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1

        return nums