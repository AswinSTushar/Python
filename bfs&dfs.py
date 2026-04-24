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
            
adl = graph_list()
adl.add_edge(0,4)
adl.add_edge(0,5)
adl.add_edge(1,5)
adl.add_edge(1,2)
adl.add_edge(2,3)
print(adl.ad_list)
adl.bfs(0)
adl.dfs(0)

class graph_adm:
    def __init__(self,vertices,directed = False):
        self.directed = directed
        self.V = vertices
            
        self.outer_matrix=[]
        for i in range(self.V):
            row=[]
            for j in range(self.V):
                row.append(0)
            self.outer_matrix.append(row)

    def add_edge(self,u,v):
        self.outer_matrix[u][v]=1
        if self.directed == False:
            self.outer_matrix[v][u]=1

    def display(self):
        for i in range(self.V):
            for j in range(self.V):
                print(self.outer_matrix[i][j],end=" ")
            print()

adm = graph_adm(6)
adm.add_edge(0,4)
adm.add_edge(0,5)
adm.add_edge(1,5)
adm.add_edge(1,2)
adm.add_edge(2,3)
adm.display()