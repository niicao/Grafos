# Nicholas Yudi Kurita Ikai 13671852

from graph import Graph

def main():
    fileName = input()
    file = open(fileName, "r")
    eulerian_path = []

    line = file.readline()
    numbers = [int(num) for num in line.split()]
    
    edges = int(numbers[1])
    graph = Graph(numbers[0])
    for i in range(0, edges):
        line = file.readline()
        line = line.split()

        graph.add_edge(int(line[0]), int(line[1]))


    
    graph.eulerianPath()

    



if __name__ == "__main__":
    main()