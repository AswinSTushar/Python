li=[1,2,3,4,5,6,7]
for i in range (len(li)//2):
    li[i], li[len(li)-i-1]=li[len(li)-i-1],li[i]
    start=0
    end=len(li)-1
while(start<end):
    li[start],li[end],li[start]
    start+=1
    end-=1
print(li)
print(li[::-1])

