#1 Highest Occuring Element in an array
def highestOccurringElement(nums):
    freq ={}
    for x in nums:
        freq[x] =freq.get(x,0)+1

    max_count = max(freq.values())
    candi =[num for num ,count in freq.items() if count ==max_count]
    return min(candi)

#2 Second Highest Occuring Element 
def secondHighestOccurringElement(arr):
    freq = {}
    for x in arr:
       freq [x] = freq.get(x,0)+1
    distinct_counts = sorted(set(freq.values()),reverse = True)

    if len(distinct_counts)<2:
        return -1
    sec_max =distinct_counts[1]
    candi = [num for num, count in freq.items()if count == sec_max]
    return min(candi)

#3 Sum of Highest and Lowest Frequency
def sumOfFrequencies(arr):
    freq={}
    for x in arr:
        freq[x]=freq.get(x,0)+1
    counts=freq.values()
    return max(counts)+ min (counts)