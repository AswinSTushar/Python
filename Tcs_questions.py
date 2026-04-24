# WHO IS THE LEADER PROGRAM

a=list (map(int,input("Enter the elements of the array: ").split()))
print (a)
curr_max=a[-1]
ans=[]
ans.append(curr_max)
n=len(a)
for i in range (n-2,-1,-1):
    if a[i]>curr_max:
        curr_max=a[i]
        ans.append(curr_max)

print (ans)

#________________________________________________________________________

#ABUNDANT ,DEFICENT OR PERFECT NUMBER PROBLEM
num=int(input("Enter a number: "))
sum=0
for i in range(1,int(num**0.5)+1):
        if num%i==0:
            sum+=i
            if i!=1 and i!=num//i:
                sum+=num//i
if sum>num:
        print("Abundant Number")
elif sum<num:
        print("Deficent Number")
else:
        print("Perfect Number")

#________________________________________________________________________

# RUN LENGTH ENCODING
s=input("Enter the string: ")
n=len(s)
count=1
ans=""
for i in range(1,n):
    if s[i]==s[i-1]:
        count+=1
    else:
        ans+=s[i-1]+str(count)
        count=1
ans+=s[n-1]+str(count)
print("Run Length Encoding of the string is:",ans)

#________________________________________________________________________

#EQUILLIBRIUM INDEX OF AN ARRAY

ip=list(map(int,input("Enter the elements of the array: ").split()))
def equi():
    left_sum=0
    right_sum=0
    total_sum=0
    for i in ip:
        total_sum+=i
    for i in range(len(ip)):
        right_sum=total_sum - left_sum - ip[i]
        if left_sum==right_sum:
            return i
        else:
            left_sum+=ip[i]
    return -1
print("Equilibrium index of the array is:",equi())

#________________________________________________________________________

#FIND MISSING NUMBER IN ARRAY

arr=list(map(int,input("Enter the elements of the array: ").split()))
n=len(arr)+1
print("n value equals:",n)
total_sum=n*(n+1)//2
arr_sum=sum(arr)
missing_num=total_sum - arr_sum
print("Missing number in the array is:",missing_num)

#________________________________________________________________________

#STRING PERMUTATION CHECK

s1=input("Enter first string: ")
s2=input("Enter second string: ")
def perm_check(s1,s2):
    #hashing
    if len(s1)!=len(s2):
        return False
    count={}
    for char in s1:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    for char in s2:
        if char in count:
            count[char]-=1
        else:
            return False
    for val in count.values():
        if val!=0:
            return False
    return True
print("Are the two strings permutations of each other?:",perm_check(s1,s2))

#________________________________________________________________________

#NUMBER SYSTEM CONVERSION
s=input("Enter the number: ")

#decimal to binary
def dec_to_bin(s):
    num=int(s)
    if num==0:
        return "0"
    binary=""
    while num>0:
        rem=num%2
        binary=str(rem)+binary
        num=num//2
    return binary
print("Binary representation of the number is:",dec_to_bin(s))

#decimal to octal
def dec_to_oct(s):
    num=int(s)
    if num==0:
        return "0"
    octal=""
    while num>0:
        rem=num%8
        octal=str(rem)+octal
        num=num//8
    return octal
print("Octal representation of the number is:",dec_to_oct(s))

#decimal to hexadecimal
def dec_to_hex(s):
    num=int(s)
    if num==0:
        return "0"
    hex_chars="0123456789ABCDEF"
    hexadecimal=""
    while num>0:
        rem=num%16
        hexadecimal=hex_chars[rem]+hexadecimal
        num=num//16
    return hexadecimal
print("Hexadecimal representation of the number is:",dec_to_hex(s))

#________________________________________________________________

#MAX VALUE OF SUBARRAY IN AN ARRAY

def max_subarray(arr):
    max_sum=float('-inf')
    curr_sum=0
    for num in arr:
        curr_sum+=num
        if curr_sum>max_sum:
            max_sum=curr_sum
        if curr_sum<0:
            curr_sum=0
    return max_sum

#example
arr=list(map(int,input("Enter the elements of the array: ").split()))
print("Maximum value of subarray in the array is:",max_subarray(arr))
#_______________________________________________________________

#MAXIMUM PRODUCT SUBARRAY

a=list(map(int,input("Enter the elements of the array: ").split()))
max_p =a[0]
min_p=a[0]
result=a[0]

for i in range(1,len(a)):
    if a[i]<0:
        max_p,min_p=min_p,max_p
    max_p=max(a[i],max_p*a[i])
    min_p=min(a[i],min_p*a[i])
    result=max(result,max_p)
print("Maximum product subarray is:",result)

#_______________________________________________________________

# SPIRAL MATRIX TRAVERSAL

def spiral_traversal(matrix):
    result=[]
    if not matrix:
        return result 
    top,bottom,left,right=0,len(matrix)-1,0,len(matrix[0])-1
    while top<=bottom and left<=right:
        # traverse from left to right
        for i in range(left,right+1):
            result.append(matrix[top][i])
        top+=1
        # traverse from top to bottom
        for i in range(top,bottom+1):
            result.append(matrix[i][right])
        right-=1
        # traverse from right to left
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
        bottom-=1
        # traverse from bottom to top
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
        left+=1
    return result

#________________________________________________________________

        

        






    



