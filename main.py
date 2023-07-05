def rref(matrix,row,column):
    check=0
    for r in range(row):
        i=r
        while matrix[i][check]==0:
            i+=1
            if i==row:
                i=r
                check+=1
                if column==check:
                    break
        matrix[i],matrix[r]=matrix[r],matrix[i]
        try:
            piv=matrix[r][check]
            pivot.append((r,check))
            matrix[r]=[x/piv for x in matrix[r]]
            for i in range(row):
                if i!=r:
                    piv=matrix[i][check]
                    matrix[i]=[round(i_r-piv*red,5) for red,i_r in zip(matrix[r],matrix[i])]
            check+=1
        except:
            pass
        if check>=column:
            break

def nullspace(matrix,var,r,c):
    column=[]
    free=[]
    j=0
    while True:
        i=0
        f=False
        temp=[0.0]*c
        null=temp.copy()
        while i<r:
            try:
                if matrix[i][j]!=0:
                    if tuple((i,j)) in pivot:
                        f=True
                temp[i]=matrix[i][j]
            except:
                pass
            i+=1
        if f==False:
            for k in range(len(temp)):
                try:
                    null[pivot[k][1]]=round(-temp[k]/matrix[pivot[k][0]][pivot[k][1]],5)
                    if null[pivot[k][1]]==-0.0:
                        null[pivot[k][1]]=0.0
                except:
                    continue
            null[j]=1.0
            column.append(null)
            free.append(var[j])
        j+=1
        if j==c:
            break
    return column,free         

r=int(input("Enter no of rows: "))
c=int(input("Enter no of columns: "))
i=0
matrix=[]
print("Enter matrix:")
while i<r:
    row=list(map(int,input().split()))
    if len(row)!=c:
        print("Incorrect number of elements entered")
        print("Try again")
        print()
        continue
    matrix.append(row)
    i+=1
pivot=[]
rref(matrix,r,c)
for i in matrix:
    for j in i:
        print(j,end=" ")
    print()
print()
var=["x"+str(i) for i in range(1,c+1)]
null, free_var= nullspace(matrix,var,r,c)
print("Solution in paramteric vector form: ")
vector=""
for i in range(len(null)):
    vector+=free_var[i]+"*"+str(null[i])+"+"
if vector=="":
    print(str([0]*c))
else:
    print(vector.rstrip("+"))