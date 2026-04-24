#number of substring

s=input("Enter the string:")
print("The substrings are:")
for i in range(len(s)):
    for j in range(i,len(s)):
        print(s[i:j+1])

#_______________________________________________________________

#reverse vowels in a string
s=input("Enter the string: ")
vowels="aeiouAEIOU"
s=list(s)
i,j=0,len(s)-1
while i<j:
    if s[i] not in vowels:
        i+=1
    elif s[j] not in vowels:
        j-=1
    else:
        s[i],s[j]=s[j],s[i]
        i+=1
        j-=1
print("".join(s))
#_______________________________________________________________

# print palindromic substrings
s=input("Enter the string: ")
n=len(s)
count=0
for i in range(n):
    #odd length
    l,r=i,i
    while l>=0 and r<n and s[l]==s[r]:
        print(s[l:r+1])
        count+=1
        l-=1
        r+=1
    #even length
    l,r=i,i+1
    while l>=0 and r<n and s[l]==s[r]:
        print(s[l:r+1])
        count+=1
        l-=1
        r+=1
print("Number of palindromic substrings:",count)
#_______________________________________________________________

#valid anagram check
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        for ch in set(s):
            if s.count(ch) != t.count(ch):
                return False
        return True 
#

#  printing first unique character of a string
s=input("Enter the string: ")
def first_unique(s):
    count={}
    for char in s:
        if char in count:
            count[char]+=1
        else:
            count[char]=1
    for i in range(len(s)):
        if count[s[i]]==1:
            return i
    return -1
print("Index of first unique character is:",first_unique(s))
print("Character is:",s[first_unique(s)] if first_unique(s)!=-1 else "None")
#_______________________________________________________________

#isomorphic strings
s1=input("Enter first string: ")
s2=input("Enter second string: ")
d={}
for i in range(len(s1)):
    if s1[i] in d:
        if d[s1[i]]!=s2[i]:
            print("Strings are not isomorphic")
            break
    else:
        d[s1[i]]=s2[i]
else:
    print("Strings are isomorphic")
#_______________________________________________________________

#binary search
s=input("Enter the elements of the array: ")
arr=list(map(int,s.split()))
target=int(input("Enter the target element: "))
def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return -1
print("Element found at index:",binary_search(arr,target))

#_______________________________________________________________
