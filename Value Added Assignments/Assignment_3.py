#1 Sum of Array Elements
def sum_of_array_elements(n, arr):
    return sum(arr)

#2 Count of Odd Numbers in Array
def countOddNumbers(n, array):
    count=0
    for x in array:
        if x%2 !=0:
            count +=1
    return count

#3 Check if the Array is Sorted
def isArraySorted(arr):
    for i in range (1,len(arr)):
        if arr[i]<arr[i-1]:
            return False
    return True

#4 Reverse an Array In-Place
def reverseArray(arr):
    arr.reverse()
    return arr