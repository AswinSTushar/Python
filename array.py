#sort array by parity
class Solution:
    def sortArrayByParity(self, nums):
        even=[]
        odd=[]
        for num in nums:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        return even+odd
    
#_______________________________________________________________
    
# sort array
l=list(map(int,input("Enter the elements of the array: ").split()))
i,j=0,len(l)-1
while i<j:
    while l[i]%2!=0:
        i+=1
    while l[j]%2==0:
        j-=1
    print(i,j)

#_______________________________________________________________











    




    


    

