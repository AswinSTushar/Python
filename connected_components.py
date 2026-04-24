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


    def count_components(self,vertices):
        q=deque()
        visited=set()
        components=0
        v= vertices

        for i in range(v):
            if i not in visited:
                q.append(i)
                visited.add(i)

                #bfs
                while q:
                    curr=q.popleft()

                    for neighbor in self.ad_list[curr]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
                components+=1
        print ("Number of connected components:",components)

adl2 = graph_list()
adl2.add_edge(7,5)
adl2.add_edge(5,2)
adl2.add_edge(1,6)
adl2.add_edge(6,3)
adl2.add_edge(0,4)
print(adl2.ad_list)
adl2.count_components(8)



      


