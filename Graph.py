class Graph:
    def __init__(self,edges) :
        self.edges = edges
        self.dict = {}
        for start,end in edges:
            if start not in self.dict.keys():
                self.dict[start] = [end]
            else:
                self.dict[start].append(end)
    
    def findAllPaths(self,start,end,path=[]):
        path =path+ [start]

        if start == end:
            return [path]
        if start not in self.dict.keys():
            return []
                
        paths=[]
        for node in self.dict[start]:
            if node not in path:
                ways = self.findAllPaths(node,end,path)
                for way in ways:
                    paths.append(way)
        return paths

    def shortest_path(self,start,end,path=[],i=0):
        path = path + [start]

        if start == end:
            return [path]
        if start not in self.dict.keys():
            return []
        
        paths =[]
        for node in self.dict[start]:
            if node not in path:
                if i > 0 and node in self.dict[path[i-1]]:
                    continue
                ways = self.shortest_path(node,end,path,i+1)
                for way in ways:
                    paths.append(way)
        return paths

routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

graph_route = Graph(routes)
print(graph_route.findAllPaths("Mumbai","New York"))
print(graph_route.shortest_path("Mumbai","New York"))

