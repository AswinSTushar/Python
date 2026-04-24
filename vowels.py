s=input()
count=0
vowels=['a','e','i','o','u','A','E','I','O','U']
for i in s:
    if i in vowels:
        count+=1
print("number of vowels is",count)

#palindrome check
for i in range(len(s)//2):
    if s[i]!=s[len(s)-1-i]:
        flag=34567890
        print("not a palindrome")
        break
if (flag==0):
        print("palindrome")
        