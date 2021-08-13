n = 8 #행
m = 8 #열 
x = 5 #만들고자 하는 행렬의 차수 
array = [[0]*m for _ in range(n)]

def division_matrix(n,m,x,array):
  for k in range(n-x+1):  
    for i in range(m-x+1):
      temp = []
      for j in range(x):
        temp.append(array[k+j][i:i+x])
      print(temp)

division_matrix(n,m,x,array)