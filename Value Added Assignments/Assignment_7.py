#Q1 Left Shift Array by n Position

from typing import List
def leftShift(arr: List[int], K: int) -> List[int]:
    # Write your solution here
    n = len(arr)
    if K >= n:
        return [0]*n
    return arr[K:]+[0]*K

#Q2 Right Shift Array by n Position

def rightShift(arr: List[int], K: int) -> List[int]:
    # Write your solution here
    n = len(arr)
    if K>=n:
        return [0]*n
    return [0]*K + arr[:n-K]

#Q3 Insert Element at a given Position 

from typing import List
def insertAtPosition(arr: List[int], X: int, P: int) -> List[int]:
    return arr[:P] + [X] + arr[P:len(arr) - 1]