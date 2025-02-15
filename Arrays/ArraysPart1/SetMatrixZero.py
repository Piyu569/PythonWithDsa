# for row traversal
def mark_row(matrix,n ,m,i):
    for j in range(m):
        if(matrix[i][j] != 0):
            matrix[i][j] = -1

def mark_column(matrix, n, m,j):
    for i in range(n):
        if matrix[i][j] != 0:
            matrix[i][j] = -1

def ZeroMatrix(matrix,n,m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                mark_column(matrix ,n,m,j)
                mark_row(matrix, n,m,i)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0
    return matrix

if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    n = len(matrix)
    m = len(matrix[0])
    ans = ZeroMatrix(matrix,n,m)

    print("The Final MAtric is: ")
    for row in ans:
        for ele in row:
            print(ele,end =" ")     
        print()

# Complexity Analysis

# Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
# Reason: Firstly, we are traversing the matrix to find the cells with the value 0. It takes O(N*M). Now, whenever we find any such cell we mark that row and column with -1. This process takes O(N+M). So, combining this the whole process, finding and marking, takes O((N*M)*(N + M)).
# Another O(N*M) is taken to mark all the cells with -1 as 0 finally.

# Space Complexity: O(1) as we are not using any extra space.