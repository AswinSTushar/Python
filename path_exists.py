from collections import defaultdict,deque
class graph_list:
    def __init__(self,directed = False):
        self.ad_list =  defaultdict(list)
        self.graph = directed

    def add_edge(self,u,v):
        self.ad_list[u].append(v)
        if self.graph == False:
            self.ad_list[v].append(u)
        
    def display(self):
        print(self.ad_list)

#bfs implementation
    def bfs(self,start):
        visited=[]
        ans=[]
        q= deque ([start])
        visited.append(start)
            
        while q:
            curr=q.popleft()
            ans.append(curr)

            for neighbor in self.ad_list[curr]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    q.append(neighbor)
        print(ans)

#dfs implementation
    def dfs(self,start):
        visited=[]
        ans=[]
        stack=[start]
        visited.append(start)

        while stack:
            curr=stack.pop()
            ans.append(curr)

            for neighbor in self.ad_list[curr]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    stack.append(neighbor)
        print(ans)


#checking if path exists between two nodes
    def path_exists(self, start, end):
        visited = set()
        q = deque([start])
        visited.add(start)

        while q:
            curr = q.popleft()
            if curr == end:
                return True

            for neighbor in self.ad_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return False
    

adl = graph_list()
adl.add_edge(0,2)
adl.add_edge(2,3)
adl.add_edge(3,6)
adl.add_edge(6,7)
adl.add_edge(7,8)
adl.add_edge(3,4)
adl.add_edge(4,9)
print(adl.ad_list)
adl.bfs(0)
adl.dfs(0)