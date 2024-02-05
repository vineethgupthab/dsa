class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_indexes = [];
        rows = len(matrix)
        columns = len(matrix[0])
        #zero_indexes = [[i,j] for i in range(rows) for j in range(columns) if matrix[i][j]==0]
        for i in range(rows):
            if 0 in matrix[i]:
                for j in range(columns):
                    if matrix[i][j]==0:
                        zero_indexes.append([i,j])
        if zero_indexes!=[]:
            for i in zero_indexes:
                matrix[i[0]]=[0]*columns # Makes the rows zero
                for k in range(rows):
                    matrix[k][i[1]]=0 # Makes the columns zero
        """
        Do not return anything, modify matrix in-place instead.
        """