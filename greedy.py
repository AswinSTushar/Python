class Solution:
    def activitySelection(self, start,finish):
        activities=[]
        for i in range(len(start)):
            activities.append((start[i],finish[i]))
        print(activities)
        activities.sort(key=lambda x:(x[1],x[0]))
        print(activities)
        count=1
        last_finish=activities[0][1]
        for i in range(1,len(activities)):
            for j in range(len(activities)):
                if activities[i][0]>=last_finish:
                    count+=1
                    last_finish=activities[i][1]
                    break
        return count

#n meetings in a room

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        meetings=[]
        for i in range(len(start)):
            meetings.append((start[i],end[i]))
            
        meetings.sort(key= lambda x:(x[1],x[0]))
            
        count=0
        ref_end=-1
        output=[]
        for start,end in meetings:
            if start>ref_end:
                count+=1
                ref_end=end
        return count



#maximum meetings in a room
from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        ans=[]
        meetings=[]
       
        for i in range(N):
            meetings.append((S[i],F[i],i+1))
           
        meetings.sort(key=lambda x:(x[1],x[0],x[2]))
            
        last_finish=-1
            
        for start,finish,i in meetings:
            if start>last_finish:
                ans.append(i)
                last_finish=finish
        ans.sort()
        return ans
    

#shop in candy store where you buy 1 candy get 2 candy free
class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n=len(prices)
        #min cost
        min_cost=0
        i=0
        j=n-1
        while i<=j:
            min_cost+=prices[i]
            i+=1
            j-=k
        #max cost
        max_cost=0
        i=n-1
        j=0
        while j<=i:
            max_cost+=prices[i]
            i-=1
            j+=k
        return [min_cost,max_cost]
    

#check if it is possible to survive on island
class Solution:
    def minimumDays(self, S, N, M):
        # code here
        Sundays=S//7
        buying_days=S-Sundays
        
        if Sundays and M*7>N*6:
            return -1
            
        total_food=S*M
        ans=0
        if total_food%N==0:
            ans=total_food//N
        else:
            ans =total_food//N + 1
        
        if ans>buying_days:
            return -1
        
        return ans
    
#chocolate distribution problem
class Solution:
    def findMinDiff(self, arr,M):
        # code here
        arr.sort()
        n=len(arr)
        if M>n or M<=0:
            return -1
        min_diff=float('inf')
        for i in range(n-M+1):
            diff=arr[i+M-1]-arr[i]
            min_diff=min(min_diff,diff)
        return min_diff


# minimum cost of ropes
 
from collections import heapq  
class Solution:
   def minCost(self, arr):
    # code here
    heapq.heapify(arr)
    cost=0
    while len(arr)>1:
        first=heapq.heappop(arr)
        second=heapq.heappop(arr)
        res=first+second
        cost+=res
        heapq.heappush(arr,res)
    return cost

