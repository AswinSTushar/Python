#Diagonal difference
li=[[1,2,3],
    [3,5,7],
   [9,10,11]]
d1=d2=0
for i in range (len(li)):
    for j in range(len(li[0])):
        if (i==j):
            d1+=li[i][j]
        if (i+j==len(li)-1):
            d2+=li[i][j]
print(abs(d1-d2))
print()

#90 degree rotation of the matrix    

for j in range(len(li[0])):
    for i in range(len(li)-1,-1,-1):
        print(li[i][j],end=" ")
    print()
print()

#180 degree rotation of the matrix
for i in range(len(li)-1,-1,-1):
    for j in range(len(li[0])-1,-1,-1):
        print(li[i][j],end=" ")
    print()
print()

#270 degree rotation of the matrix
for j in range(len(li[0])-1,-1,-1):
    for i in range(len(li)):
        print(li[i][j],end=" ")
    print()