'''
Serialize a Tree to a string.
Deserialize a string to a Tree
'''


def serialize(node):
    if node == None:
        return
    left = "("
    right = ")"
    if node.left:
        left += str(node.left.value) + '<'
    if node.right:
        right += '>' + str(node.right.value)

    return left + str(node.value) + right
