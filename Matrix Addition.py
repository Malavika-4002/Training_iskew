m,n=list(map(int,input().split()))
matrix1=[]
matrix2=[]
for i in range(m):
    row=list(map(int,input().split()))
    matrix1.append(row)
for i in range(m):
    row=list(map(int,input().split()))
    matrix2.append(row)
print("First Matrix:")
for row in matrix1:
    print(*row)
print("Second Matrix:")
for row in matrix2:
    print(*row)
    
sum=[]
for i in range(m):
    row=[]
    for j in range(m):
        row.append(matrix1[i][j]+matrix2[i][j])
    sum.append(row)    
print("Sum of the two matrices is:")   
for row in sum:
    print(*row)
