'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''


def firstMissingPositive(arr):
    firstNonNegativeIndex = 0
    i = 0
    while i < len(arr):
        if arr[i] > len(arr) or arr[i] == 0:
            arr[i] = -1
        if arr[i] <= 0:
            temp = abs(arr[i])
            arr[i] = abs(arr[firstNonNegativeIndex])
            arr[firstNonNegativeIndex] = temp
            firstNonNegativeIndex += 1
        i += 1
    i = firstNonNegativeIndex
    while i < len(arr):
        index = abs(arr[i])
        arr[index - 1] = - abs(arr[index - 1])
        i += 1
    i = 0
    print(arr)
    while i < len(arr):
        if arr[i] > 0:
            return i + 1
        i += 1
    return len(arr) + 1


print(firstMissingPositive([3, 4, -1, 1]))
print(firstMissingPositive([1, 2, 0]))
