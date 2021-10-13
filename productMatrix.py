def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

def my_productMatrix(A,B):
    answer = []
    new_arr2 = []
    for i in range(len(arr2[0])):
        temp = []
        for a in arr2:
            temp.append(a[i])
        new_arr2.append(temp)
    for x in arr1:
        temp = []
        for y in new_arr2:
            val = 0
            for a, b in zip(x, y):
                val += a * b
            temp.append(val)
        answer.append(temp)

    return answer