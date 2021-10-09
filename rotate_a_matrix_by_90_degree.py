def rotate_a_matrix_by_90_degree(matrix):
    new_matrix = []
    for i in range(len(matrix)):
        temp = []
        for row in matrix:
            temp.append(row[i])
        new_matrix.append(list(reversed(temp)))
    return new_matrix