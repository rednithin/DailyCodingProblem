'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

from collections import deque
import random


def maximumNonAdjacentSum(arr):
    d = deque()
    d.append(arr[0])
    d.append(arr[1])
    if arr[0] < 0:
        d.append(arr[2])
    else:
        d.append(arr[0] + arr[2])
    for num in arr[3:]:
        val = max(d[0], d[1], d[2], d[0] + num, d[1] + num)
        d.append(val)
        d.popleft()
    return d[-1]


def GeeksForGeeksSoln(arr):
    incl = arr[0]
    excl = 0
    for num in arr[1:]:
        incl, excl = excl + num, max(incl, excl)
    return max(incl, excl)


a = [random.randint(-100, 100) for _ in range(10)]
b = [random.randint(-100, 100) for _ in range(10)]
c = [random.randint(-100, 100) for _ in range(10)]

print(maximumNonAdjacentSum([2, 4, 6, 2, 5]))
print(maximumNonAdjacentSum([5, 1, 1, 5]))
print(maximumNonAdjacentSum([5, 5, 10, 100, 10, 5]))
print(maximumNonAdjacentSum(a))
print(maximumNonAdjacentSum(b))
print(maximumNonAdjacentSum(c))

print(GeeksForGeeksSoln([2, 4, 6, 2, 5]))
print(GeeksForGeeksSoln([5, 1, 1, 5]))
print(GeeksForGeeksSoln([5, 5, 10, 100, 10, 5]))
print(GeeksForGeeksSoln(a))
print(GeeksForGeeksSoln(b))
print(GeeksForGeeksSoln(c))
