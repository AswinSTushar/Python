row=int(input())
col=int(input())
ans=[]
for i in range(row):
    temp=[]
    for j in range(col):
        x=int(input())
        temp.append(x)
    ans.append(temp)
print(ans)
