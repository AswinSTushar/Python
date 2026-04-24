#koko eating bananas
def minEatingSpeed(piles, h: int) -> int:
    left,right=1,max(piles)
    
    while left<right:
        mid=(left+right)//2
        hours=0
        
        for pile in piles:
            hours+=-(-pile//mid) 
            
        if hours>h:
            left=mid+1
        else:
            right=mid
    return left

#_______________________________________________________________
