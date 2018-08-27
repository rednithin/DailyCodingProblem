def productArray(arr):
    left = []
    right = []
    l = len(arr)
    for elem in arr:
        if len(left) == 0:
            left.append(elem)
        else:
            left.append(left[-1] * elem)
    right = [1] * len(arr)
    for i, elem in enumerate(arr[::-1]):
        if i == 0:
            right[l - i - 1] = elem
        else:
            right[l - i - 1] = right[l - i] * elem
    left = [1] + left
    right.append(1)

    result = []
    for a, b in zip(left[:-1], right[1:]):
        result.append(a*b)

    return result


print(productArray([1, 2, 3, 4, 5]))
print(productArray([3, 2, 1]))
print(productArray([1, 4, 2, 3]))
