'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1

'''


def countUnivalSubTrees(tree):
    if tree == None:
        return (True, '-', 0)
    isUnival1, element1, count1 = countUnivalSubTrees(tree.left)
    isUnival2, element2, count2 = countUnivalSubTrees(tree.left)

    if element1 == '-' and element2 == '-':
        return True, tree.value, 1

    if isUnival1 == True and isUnival1 == isUnival2 and element1 == element2 and element1 == tree.value:
        return True, element1, count1 + count2
    else:
        return False, tree.value, count1 + count2
