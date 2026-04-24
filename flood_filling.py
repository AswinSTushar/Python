#FLOOD FILLING ALGORITHM USING BFS

from collections import deque
def flood_fill(self,sr,sc,image,newColor):
    og_color=image[sr][sc]
    q=deque([(sr,sc)])
    rows=len(image)
    cols=len(image[0])

    while q:
        r,c=q.popleft()
        if r<0 or r>=rows or c<0 or c>=cols:
            continue
        if image[r][c]!=og_color: 
            continue
        image[sr][sc]=newColor
        q.append((r+1,c))
        q.append((r-1,c))
        q.append((r,c+1))
        q.append((r,c-1))
    return image