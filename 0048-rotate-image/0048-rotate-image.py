class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i+1):
                matrix[i][j],matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)
        for i in range(n):
            low, high = 0, n-1
            while low < high:
                matrix[i][low], matrix[i][high] = matrix[i][high], matrix[i][low]
                low += 1
                high -= 1
        