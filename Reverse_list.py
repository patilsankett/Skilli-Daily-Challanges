def reverseList(nums: list[int]) -> list[int]:
    result = []
    for i in range(len(nums)-1,-1,-1):
        result.append(nums[i])
    return result