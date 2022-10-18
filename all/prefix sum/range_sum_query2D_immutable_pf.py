class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        sum_matrix = copy.copy(matrix)
        for i in range(len(matrix)):
            sum = 0
            for j in range(len(matrix[0])):
                sum += matrix[i][j]
                temp = 0
                if i - 1 >= 0:
                    temp = matrix[i-1][j]
                temp += sum
                matrix[i][j] = temp
        
        self.sum_matrix = sum_matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        total = self.sum_matrix[row2][col2]
        if row1 - 1 >= 0:
            total -= self.sum_matrix[row1-1][col2]
        if col1 - 1 >= 0:
            total -= self.sum_matrix[row2][col1-1]
        if row1 - 1 >= 0 and col1 -1 >=0:
            total += self.sum_matrix[row1-1][col1-1]
        
        return total
