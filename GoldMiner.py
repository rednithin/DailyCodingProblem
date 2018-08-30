import copy
from collections import deque
from pprint import pprint

path = deque()
matrix = [[0, 1, -1], [1, 0, -1], [1, 1, 1]]
dpmatrix = copy.deepcopy(matrix)

rows = len(matrix)
cols = len(matrix[0])


def populate(dpmatrix, matrix):
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != -1:
                if i < rows - 1 and matrix[i+1][j] != -1:
                    dpmatrix[i+1][j] = max(dpmatrix[i+1][j],
                                           matrix[i+1][j] + dpmatrix[i][j])
                if j < cols - 1 and matrix[i][j+1] != -1:
                    dpmatrix[i][j+1] = max(dpmatrix[i][j+1],
                                           matrix[i][j+1] + dpmatrix[i][j])


def findPath(dpmatrix, matrix, i, j, path):
    if i < 0 or j < 0:
        return
    path.appendleft((i, j))
    if i == 0 and j == 0:
        return
    val = dpmatrix[i][j] - matrix[i][j]
    if i > 0 and dpmatrix[i - 1][j] == val:
        findPath(dpmatrix, matrix, i - 1, j, path)
    if j > 0 and dpmatrix[i][j - 1] == val:
        findPath(dpmatrix, matrix, i, j - 1, path)


totalGold = 0
populate(dpmatrix, matrix)
totalGold += dpmatrix[rows-1][cols-1]
findPath(dpmatrix, matrix,  rows - 1, cols - 1, path)
for i, j in path:
    matrix[i][j] = 0
dpmatrix = copy.deepcopy(matrix)
populate(dpmatrix, matrix)
totalGold += dpmatrix[rows-1][cols-1]

print(totalGold)
