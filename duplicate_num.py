
li= [1,2,1,1,2,2,3,3,4,5]
dup=[]
print (li[:])
count=0
for i in li[:]:
    if (li.count(i)>1):
        dup.append(i)
      #  count+=1
#        for j in range(li.count(i)):
 #           li.remove(i)
 #       print(li)
#print("The number of duplicate elements are:",count)
    