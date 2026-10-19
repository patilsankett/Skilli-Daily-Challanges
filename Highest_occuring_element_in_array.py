# Highest Occuring Element in an Array 
def highestOccurringElement(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num,0)+1

    best = None 
    for num, freq in count.items():
        if best is None or freq > count[best] or (freq == count[best]and num <best):
            best = num
    return best