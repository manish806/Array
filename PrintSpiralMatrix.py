def SpiralMatrix(A):
    '''
    A-> Array taken as input which is a 2D Array
    k -> Starting of Row Index
    l -> Starting of Column Index
    m -> No. of rows/End of Row Index
    n -> No. of columns/ End of Column Index
    '''
    m=len(A)
    n=len(A[0])
    k,l = 0,0
    while (k < m and l < n):
        # Print the 1st Row of the Remaining Rows
        for i in range(l, n):
            print(A[k][i], end=' ')
        k += 1
        # Print the Last Columns of the Remaining Columns
        for i in range(k, m):
            print(A[i][n - 1], end=' ')
        n -= 1
        # Print the last row of the Remaining Rows
        if (k < m):
            for i in range(n - 1, l - 1, -1):
                print(A[m - 1][i], end=' ')
            m -= 1
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(A[i][l], end=' ')
            l += 1
if __name__ == "__main__":
    B = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    SpiralMatrix(B)
