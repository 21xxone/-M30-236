import time
def maxSubArray(nums):
    arrayOfSums = [nums[0]]
    maxSum = nums[0]
    maxPosition = 0
    for i in range(1, len(nums)):
        if arrayOfSums[i - 1] > 0:
            arrayOfSums.append(arrayOfSums[i - 1] + nums[i])
        else:
            arrayOfSums.append(nums[i])
        if arrayOfSums[i] > maxSum:
            maxSum = arrayOfSums[i]
            maxPosition = i
    if maxSum < 0:
        return nums[maxPosition]
    endOfMaxSubarray = maxPosition
    startOfMaxSubarray = endOfMaxSubarray
    while startOfMaxSubarray >= 0 and arrayOfSums[startOfMaxSubarray] >= 0:
        startOfMaxSubarray -= 1
    return nums[startOfMaxSubarray + 1: endOfMaxSubarray + 1]

sourceArray = [2, -5, 2, 2, -1, 3, -1, 2, -5, 4]
start = time.time()
print(maxSubArray(sourceArray))
end = time.time()
print(end - start)