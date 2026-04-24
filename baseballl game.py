#baseball game
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        li=[]
        for i in operations:
            if i =='+':
                su=li[-1]+li[-2]
                li.append(su)
            elif i =='D':
                su=li[-1]*2
                li.append(su)
            elif i =='C':
                li.pop()
            else:
                li.append(int(i))
        return sum(li)

#_______________________________________________________________

#LAST STONE WEIGHT
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        li=[]
        for i in stones:
            heapq.heappush(li,-1)
        while len(li)>=2:
            x=-heapq.heappop(li)
            y=-heapq.heappop(li)
            if x>y:
                heapq.heappush(li,-(x-y))
        if len(li)==0:
            return 0
        return -heapq.heappop(li)

#_______________________________________________________________

#valid paranthesis
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in s:
            if i in ['(','{','[']:
                stack.append(i)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if (top=='(' and i!=')') or (top=='{' and i!='}') or (top=='[' and i!=']'):
                    return False
        return len(stack)==0
    
#_______________________________________________________________

# arrays
# strings
# binary search
# linked lists
# queue

    