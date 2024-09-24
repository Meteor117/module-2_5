def get_matrix(n, m, value):
    matrix = []
    for i in range (n):
        matrix.append ([])#пустой список для строки
        for j  in range (m):
            matrix [i].append (value)#заполнение по текущим индексам
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)








# matrix = []
# for i in range (3):
#     row= []
#     for j in range (3):
#         row.append(0)
#     matrix.append (row)
#
# def is_matrix (m):
#     if not m:
#         return False
#     row_length = len (m[0])
#     return all (len (row)==row_length for row in m)
# print ('Matrix:')
# for row in matrix:
#     print (row)
# print ('\nIs this a mstrix?', is_matrix)
