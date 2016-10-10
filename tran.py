matrix=[]
row=int(input('enter no. of rows'))
col=int(input('enter no. of columns'))
for r in range(col):
    t=[]
    for i in range(col):
        elements=int(input('enter element'))
        t.append(elements)
    matrix.append(t)
trans=[]
for r in range(row):
    t=[]
    for i in range(col):
        t.append(matrix[i][r])
    trans.append(t)
print('the transpose is:')
for l in range(row):
    print(trans[l])
    
