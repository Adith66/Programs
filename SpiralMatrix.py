res=[]
mat=[[0,1,0,2],
    [0,2,0,2],
    [2,0,0,0]]
rows=len(mat)
cols=len(mat[0])
top,bottom,left,right=0,rows-1,0,cols-1
while len(res)<rows*cols:
    for i in range(left,right+1):
        res.append(mat[top][i])
    top+=1
    for i in range(top,bottom+1):
        res.append(mat[i][right])
    right-=1
    if top<=bottom:
        for i in range(right,left-1,-1):
            res.append(mat[bottom][i])
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            res.append(mat[i][left])
        left+=1
print(res)
