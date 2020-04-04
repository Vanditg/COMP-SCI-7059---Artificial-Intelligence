//==================================
// Artificial Intelligence
// Student: Vandit Jyotindra Gajjar
// Student ID: a1779153
// Semester: 1
// Year: 2020
// Assignment: 1
//===================================

from bfs import BFS
from ucs import UniformCostSearch
from astar import AStar
import sys


class PathFinder:
    def __init__(self, src, dest, M, N, map_, algo, heuristic=None):
        self.src = src
        self.dest = dest
        self.M = M
        self.N = N
        self.map = map_
        self.algo = algo
        self.heuristic = heuristic

    def run(self):
        if self.algo == "bfs":
            model = BFS(self.src, self.dest, self.M, self.N, self.map)
            path = model.run()
            return path
        if self.algo == "ucs":
            model = UniformCostSearch(self.src, self.dest, self.M, self.N, self.map)
            path = model.run()
            return path
        if self.algo == "astar":
            model = AStar(self.src, self.dest, self.M, self.N, self.map, self.heuristic)
            path = model.run()
            return path


if __name__ == "__main__":
    map_file = sys.argv[1]
    algo = sys.argv[2]

    if len(sys.argv) > 3:
        heuristic = sys.argv[3]
    else:
        heuristic = None
    
    file_ = open(map_file)

    line = file_.readline()
    line = line.strip().split(" ")
    M, N = int(line[0]), int(line[1])
    src = file_.readline().split()
    src = (int(src[0])-1, int(src[1])-1)
    dest = file_.readline().split()
    dest = (int(dest[0])-1, int(dest[1])-1)

    map_ = []
    for line in file_.readlines():
        line = line.strip().split()
        map_.append(line)
    
    pf = PathFinder(src, dest, M, N, map_, algo, heuristic)
    
    path = pf.run()

    out_file = open("./init.txt", "w+")

    for x, y in path:
        map_[x][y] = "*"
    
    if not path:
        print("null")
        out_file.write("null\n")
    else:
        for line in map_:
            s = " ".join(line)
            print(s)
            out_file.write(s + "\n")
    out_file.close()
    file_.close()