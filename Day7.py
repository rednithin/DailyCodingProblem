'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''


def totalPossibleDecoding(encodedString):
    if len(encodedString) == 1:
        return 1
    dpArray = [1] * len(encodedString)
    combined = int(encodedString[0])*10 + int(encodedString[1])
    if combined > 9 and combined < 26:
        dpArray[1] = 2
    for i in range(2, len(encodedString)):
        combined = int(encodedString[i-1])*10 + int(encodedString[i])
        if combined > 9 and combined < 26:
            dpArray[i] = dpArray[i-1] + dpArray[i-2]
        else:
            dpArray[i] = dpArray[i-1]
    return dpArray[-1]


print(totalPossibleDecoding('111'))
print(totalPossibleDecoding('102'))
