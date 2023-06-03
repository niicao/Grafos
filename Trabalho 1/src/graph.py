from collections import defaultdict
class Graph:
        
    def __init__(self, size:int):
        self.AdjList = {}
        self.currentPos = None

        for i in range(0, size):
            self.AdjList[i] = []

    def __str__(self):
        str_list = []
        for key, value in self.AdjList.items():
            str_list.append(f"{key}: {value}")
        return "{" + ", ".join(str_list) + "}"



    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d", v1, v2)
        self.AdjList[v1].append(v2)
        self.AdjList[v2].append(v1)
        

    def remove_edge(self, v1, v2):
        
        self.AdjList[v1].remove(v2)

    def is_empty(self):
        if not self.AdjList:
            return True

    
    def isEulerian(self):
        oddDegreeCounter = 0
        for node in self.AdjList:
            if len(self.AdjList[node]) % 2 != 0:
                oddDegreeCounter += 1
        if oddDegreeCounter == 0 or oddDegreeCounter == 2:
            return True
        else:
            return False

    # Hierholzer's algorithm
    def eulerianPath(self):
        if not self.isEulerian():
            return None
        path = []
        stack = []
        currNode = next(iter(self.AdjList))
        stack.append(currNode)
        while len(stack) > 0:
            if len(self.AdjList[currNode]) > 0:
                stack.append(currNode)
                nextNode = self.AdjList[currNode].pop()
                self.AdjList[nextNode].remove(currNode)
                currNode = nextNode
            else:
                path.append(currNode)
                currNode = stack.pop()
        if(list(path)[0] == list(path)[-1]):
            print("Sim")
            print(*list(path))
            return list((path))
        else:
            print("Não")
            return None

    


