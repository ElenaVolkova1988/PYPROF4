""" Напишите функцию для транспонирования матрицы """

matrix = [[1, 2], [4, 5], [7, 8]]

""" def matrix_transposition(matrix: list[list[int]]):
    for row in matrix:
        print(row)
    rez = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("\n")
    for row in rez:
        print(row)
        """
def matrix_transpose( matrix ):
    if not matrix: return []
    return [ [ row[ i ] for row in matrix ] for i in range( len( matrix[ 0 ] ) ) ]  

print (matrix_transpose(matrix))  