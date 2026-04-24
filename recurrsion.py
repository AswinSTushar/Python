#POWER OF TWO NUMBERS USING RECURSION

def power(m, n):
    # Base case: any number to the power of 0 is 1
    if n == 0:
        return 1
    # Recursive case: multiply base by the result of power with exponent decreased by 1
    else:
        return m * power(m, n - 1)
# Example:
result = power(2, 3)
print("2 to the power of 3 is:", result)
#__________________________________________________________________-

#SUM OF DIGITS OF A NUMBER USING RECURSION
def sum_of_digits(n):
    # Base case: if the number is 0, return 0
    if n == 0:
        return 0
    else:
    # Recursive case: add the last digit to the sum of digits of the remaining number
        return n % 10 + sum_of_digits(n // 10)
# Example:
n = 1234
result = sum_of_digits(n)
print("Sum of digits of", n, "is:", result)

#________________________________________________________________________

# FIBONACCI SERIES USING RECURSION
def fib(n):
    if n == 1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
print("Fibonacci value of given number is:",fib(5))
#________________________________________________________________________

#MEMO-IZATION FOR FIBONACCI
def memo_fib(n, dp={}):
    if n ==1:
        return 0
    if n==2:
        return 1
    if n in dp:
        return dp[n]
    dp[n]= memo_fib(n-1,dp)+memo_fib(n-2,dp)
    return dp[n]
print("Memo-ization value of given number is:",memo_fib(8))
#________________________________________________________________________

#TABULATION FOR FIBONACCI
def tab_fib(n):
    dp=[0]*(n+1)
    #assigning base values
    dp[1]=0
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[n]
print("Tabulation value of given number is:",tab_fib(10))
#________________________________________________________________________

#SPACE OPTIMIZED FOR FIBONACCI
def space_fib(n):
    prev2=0
    prev1=1

    for i in range(3,n+1):
        curr=prev1+prev2
        prev2=prev1
        prev1=curr
    return prev1
print("Space optimized value of given number is:",space_fib(11))
#________________________________________________________________________

from typing import List
#MIN COST OF CLIMBING STAIRS
def minCostClimbingStairs(self, cost: List[int]) -> int:
    s=len(cost)
    dp=[0]*(s+1)
    dp[0]=0
    dp[1]=cost[0]
    for i in range(2,s+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    return dp[s]
#example
print("Minimum cost of climbing stairs is:",minCostClimbingStairs(0,[10,15,20]))

#________________________________________________________________________

#HOUSE ROBBER PROBLEM
class Solution:
    def rob(self, nums: List[int]) -> int:
        h=len(nums)
        def max_c_rob(i):
            if i==0:
               return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if i<0:
                return 0
            p=nums[i]+max_c_rob(i-2)
            np=max_c_rob(i-1)
            return max(p,np)
        return max_c_rob(h-1)
#example
print("Maximum amount that can be robbed is:",Solution().rob([2,7,9,3,1]))  
#________________________________________________________________________
        
       
           









    
