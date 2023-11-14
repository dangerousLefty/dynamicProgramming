#Problem:
#   Unique Paths
#
#   A robot is located at the top-left corner of an m x n grid (marked 'S' in the diagram below)
#   The robot can only move either down or right at any point in time.
#   The robot is tryingto reach the bottom-right corner of the grid (marked 'F' in the diagram below).
#
#   How many possible unique paths are there? 
#
#   +---+---+---+---+
#	| S |   |   |   |
#	+---+---+---+---+
#	|   |   |   |   |
#	+---+---+---+---+
#	|   |   |   | E |
#	+---+---+---+---+

def uniquePaths(input: [[int]]) -> int:

    m = len(input)
    n = len(input[0])

    input[0][0] = 1
    for i in range(0,m):
        for j in range(0,n):
            if i == 0 and j == 0:
                continue
            elif i > 0 and j > 0: 
                input[i][j] = input[i][j-1] + input[i-1][j]

            elif j == 0:
                input[i][j] = input[i-1][j]
            
            else: #i = 0
                input[i][j] = input[i][j-1]
                

    return input[m-1][n-1]

#Follow-up question:
#   If there are blockages in our path, how will we solve the problem?
#
#   How many possible unique paths are there? 
#
#   +---+---+---+---+
#	| S |   |   |   |
#	+---+---+---+---+
#	|   | x | x | x |
#	+---+---+---+---+
#	|   |   |   | E |
#	+---+---+---+---+


#---------------------------------------------------------
# !!!!!!!!!!   correct but long way. too many comparisons!  !!!!!!!!!!
#---------------------------------------------------------


# F(i,j) = F(i,j-1) + F(i-1, j)
# def uniquePathsWithObstacles(matrix: [[int]]) -> int:

#     m = len(matrix)
#     n = len(matrix[0])

#     matrix[0][0] = 1
#     for i in range(0,m):
#         for j in range(0,n):
#             if i == 0 and j == 0:
#                 continue
#             elif i > 0 and j > 0: 
#                 if matrix[i][j] == 'x':
#                     continue
#                 else:
#                     if matrix[i][j-1] == 'x' and matrix[i-1][j] == 'x':
#                         continue
#                     elif matrix[i][j-1] == 'x':
#                         matrix[i][j] = matrix[i-1][j]
#                     elif matrix[i-1][j] == 'x':
#                         matrix[i][j] = matrix[i][j-1]
#                     else:
#                         matrix[i][j] = matrix[i][j-1] + matrix[i-1][j]

#             elif j == 0:
#                 if matrix[i][j] == 'x':
#                     continue
#                 elif matrix[i-1][j] == 'x':
#                     continue
#                 else:
#                     matrix[i][j] = matrix[i-1][j]
            
#             else: #i = 0
#                 if matrix[i][j] == 'x':
#                     continue
#                 elif matrix[i][j-1] == 'x':
#                     continue
#                 else:
#                     matrix[i][j] = matrix[i][j-1]
                

#     return matrix[m-1][n-1]

#above code is very tedious as you have to perform many checks. 

#------------------------------------------------------------------------
# below is demonstrated a simpler way to implement the obstacle question
#-------------------------------------------------------------------------

def uniquePathsWithObstacles(input: [[int]]) -> int:
    m = len(input) #row
    n = len(input[0]) #column

    input[0][0] = 1

    for i in range(0,m):
        for j in range(0,n):
            if i == 0 and j == 0:
                continue
            elif input[i][j] == 'x':
                input[i][j] = 0
                continue

            elif i > 0 and j > 0: 
                input[i][j] = input[i][j-1] + input[i-1][j]

            elif j == 0:
                input[i][j] = input[i-1][j]

            else:
                input[i][j] = input[i][j-1]

    return input[m-1][n-1]

#Optimization problem:
#       Maximum Profit in a grid
#
#       A robot is located at the top-left corner of a m x n grid
#       The robot can only move either down or right at any point in time.
#       The robot is trying to reach the bottom-right corner of the grid
#       Each cell contains a coin the robot can collect.
#
#       What is the maximum profit the robot can gather?
#
#       	+---+---+---+---+
#	        | S | 2 | 2 | 1 |
#	        +---+---+---+---+
#	        | 3 | 1 | 1 | 1 |
#	        +---+---+---+---+
#	        | 4 | 4 | 2 | E |
#	        +---+---+---+---+

def uniquePathsCosts(input: [[int]]) -> int:
    m = len(input) #row
    n = len(input[0]) #column

    dpMatrix = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        for j in range(n):
            dpMatrix[i][j] = input[i][j]

            if i > 0 and j > 0:
                dpMatrix[i][j] += max(dpMatrix[i][j-1], dpMatrix[i-1][j])

            elif j > 0:
                dpMatrix[i][j] += dpMatrix[i][j-1]

            else:
                dpMatrix[i][j] += dpMatrix[i-1][j]

    return dpMatrix[i][j]

def uniquePathsCostsWithRoute(input: [[int]]) -> ():
    m = len(input) #rows
    n = len(input[0]) #columns

    dpMatrix = [[(0, (0, 0)) for j in range(n)] for i in range(m)]

    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            tempTuple = (input[i][j], (i,j))
            dpMatrix[i][j] = tempTuple

            if i > 0 and j > 0:
                profit = input[i][j] + max(dpMatrix[i][j-1][0], dpMatrix[i-1][j][0])
                
                if input[i][j-1] >= input[i-1][j]:
                    prevIndex = (i,j-1)
                
                else:
                    prevIndex = (i-1, j)

                tempTuple = (profit, prevIndex)
                dpMatrix[i][j] = tempTuple

            elif j > 0:
                profit = input[i][j] + dpMatrix[i][j-1][0]
                prevIndex = (i,j-1)
                tempTuple = (profit, prevIndex)

                dpMatrix[i][j] = tempTuple

            else: # i > 0
                profit = input[i][j] + dpMatrix[i-1][j][0]
                prevIndex = (i-1,j)
                tempTuple = (profit, prevIndex)

                dpMatrix[i][j] = tempTuple

    #return route
    i = m - 1
    j = n - 1
    routeArray = []
    routeArray.append((i,j))
    while i > 0 or j > 0:
        tempTuple = dpMatrix[i][j]
        routeArray.append(tempTuple[1])

        i = tempTuple[1][0]
        j = tempTuple[1][1]

    routeArray.reverse()

    return (dpMatrix[m-1][n-1][0], routeArray)



matrix = [[0,2,2,50],
          [3,1,1,100],
          [4,4,2,0]]

a = uniquePathsCostsWithRoute(matrix)

print(" total profit is {0} \n and route to take is {1}".format(a[0], a[1]))
    